from __future__ import annotations

import json
import os
import tomllib
from pathlib import Path
from typing import Any

from suporte import ACOES_PERMITIDAS, carregar_casos


RAIZ = Path(__file__).resolve().parents[2]
CONFIGURACAO = RAIZ / "config" / "llm.toml"
CATEGORIAS = {"internet", "climatizacao", "computador", "objeto_perdido", "outro"}


def _modelo_configurado() -> str:
    with CONFIGURACAO.open("rb") as arquivo:
        configuracao = tomllib.load(arquivo)
    if configuracao.get("provider") != "gemini":
        raise ValueError("Esta prática espera o provider gemini em config/llm.toml.")
    return str(configuracao["model"])


def _gerar_com_gemini(prompt: str, schema: dict[str, Any]) -> dict[str, Any]:
    chave = os.environ.get("GEMINI_API_KEY")
    if not chave:
        raise RuntimeError("Defina GEMINI_API_KEY ou execute com --offline.")

    from google import genai
    from google.genai import types

    cliente = genai.Client(api_key=chave)
    try:
        resposta = cliente.models.generate_content(
            model=_modelo_configurado(),
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_json_schema=schema,
                temperature=0,
            ),
        )
    finally:
        cliente.close()
    if not resposta.text:
        raise RuntimeError("O modelo não devolveu conteúdo.")
    return json.loads(resposta.text)


def _caso_simulado(mensagem: str) -> dict[str, Any]:
    normalizada = mensagem.casefold().strip()
    for caso in carregar_casos():
        if caso["mensagem"].casefold() == normalizada:
            return dict(caso["estado"])
    if "wi-fi" in normalizada or "internet" in normalizada:
        return {"categoria": "internet", "urgente": "daqui a pouco" in normalizada, "local": None}
    return {"categoria": "outro", "urgente": False, "local": None}


def interpretar(mensagem: str, offline: bool) -> dict[str, Any]:
    print("MODO OFFLINE — RESPOSTA SIMULADA" if offline else "MODO ONLINE — GEMINI")
    if offline:
        estado = _caso_simulado(mensagem)
    else:
        estado = _gerar_com_gemini(
            "Extraia somente os dados da solicitação sintética a seguir. "
            "Não invente local nem urgência.\n\n" + mensagem,
            {
                "type": "object",
                "properties": {
                    "categoria": {"type": "string", "enum": sorted(CATEGORIAS)},
                    "urgente": {"type": "boolean"},
                    "local": {"type": ["string", "null"]},
                },
                "required": ["categoria", "urgente", "local"],
                "additionalProperties": False,
            },
        )
    if estado.get("categoria") not in CATEGORIAS or not isinstance(estado.get("urgente"), bool):
        raise ValueError("A resposta não corresponde à estrutura esperada.")
    if estado.get("local") is not None and not isinstance(estado["local"], str):
        raise ValueError("O local deve ser texto ou null.")
    return estado


def decidir(objetivo: str, estado: dict[str, Any], offline: bool) -> dict[str, str]:
    print("MODO OFFLINE — RESPOSTA SIMULADA" if offline else "MODO ONLINE — GEMINI")
    if offline:
        if not estado.get("local"):
            decisao = {"acao": "pedir_informacao", "motivo": "o local não foi informado"}
        elif estado.get("urgente"):
            decisao = {
                "acao": "abrir_chamado_prioritario",
                "motivo": "há impacto imediato e o local é conhecido",
            }
        elif estado.get("categoria") == "objeto_perdido":
            decisao = {"acao": "fornecer_orientacao", "motivo": "há orientação conhecida para o caso"}
        else:
            decisao = {"acao": "abrir_chamado_normal", "motivo": "há dados suficientes para registrar"}
    else:
        decisao = _gerar_com_gemini(
            f"Objetivo: {objetivo}\nEstado: {json.dumps(estado, ensure_ascii=False)}\n"
            f"Escolha uma ação entre: {sorted(ACOES_PERMITIDAS)}. Explique brevemente.",
            {
                "type": "object",
                "properties": {
                    "acao": {"type": "string", "enum": sorted(ACOES_PERMITIDAS)},
                    "motivo": {"type": "string"},
                },
                "required": ["acao", "motivo"],
                "additionalProperties": False,
            },
        )
    if decisao.get("acao") not in ACOES_PERMITIDAS or not isinstance(decisao.get("motivo"), str):
        raise ValueError("A decisão não corresponde à estrutura ou aos limites esperados.")
    return {"acao": decisao["acao"], "motivo": decisao["motivo"]}
