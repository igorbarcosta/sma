from __future__ import annotations

import json
import os
import tomllib
from pathlib import Path
from typing import Any


ACOES_CONVERSACIONAIS = {"perguntar_local", "orientar_e_encerrar"}
RAIZ = Path(__file__).resolve().parents[2]
CONFIGURACAO = RAIZ / "config" / "llm.toml"


def _modelo_configurado() -> str:
    with CONFIGURACAO.open("rb") as arquivo:
        configuracao = tomllib.load(arquivo)
    if configuracao.get("provider") != "gemini":
        raise ValueError("Esta prática espera o provider gemini em config/llm.toml.")
    return str(configuracao["model"])


def _gerar_com_gemini(prompt: str) -> dict[str, Any]:
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
                response_json_schema={
                    "type": "object",
                    "properties": {
                        "acao": {"type": "string", "enum": sorted(ACOES_CONVERSACIONAIS)},
                        "mensagem": {"type": "string"},
                        "concluiu": {"type": "boolean"},
                        "motivo": {"type": "string"},
                    },
                    "required": ["acao", "mensagem", "concluiu", "motivo"],
                    "additionalProperties": False,
                },
                temperature=0,
            ),
        )
    finally:
        cliente.close()
    if not resposta.text:
        raise RuntimeError("O modelo não devolveu conteúdo.")
    return json.loads(resposta.text)


def _decisao_simulada(estado: dict[str, Any]) -> dict[str, Any]:
    if not estado.get("local"):
        return {
            "acao": "perguntar_local",
            "mensagem": "Em qual local isso está acontecendo?",
            "concluiu": False,
            "motivo": "o local é necessário para orientar o próximo passo",
        }

    return {
        "acao": "orientar_e_encerrar",
        "mensagem": (
            f"Entendi: o problema é no {estado['local']}. Posso registrar os dados e orientar "
            "o próximo passo, mas ainda não tenho uma ferramenta para consultar equipamentos "
            "ou abrir um chamado."
        ),
        "concluiu": True,
        "motivo": "o agente reuniu a informação necessária, mas seu limite é conversacional",
    }


def decidir(objetivo: str, observacao: str, estado: dict[str, Any], offline: bool) -> dict[str, Any]:
    """Produz uma decisão limitada a duas ações conversacionais."""
    print("MODO OFFLINE — DECISÃO SIMULADA" if offline else "MODO ONLINE — GEMINI")
    if offline:
        decisao = _decisao_simulada(estado)
    else:
        decisao = _gerar_com_gemini(
            "Você é o componente de decisão de um agente didático.\n"
            f"Objetivo: {objetivo}\n"
            f"Observação mais recente: {observacao}\n"
            f"Estado disponível: {json.dumps(estado, ensure_ascii=False)}\n"
            "Você só pode perguntar o local ou orientar e encerrar. Não afirme que executou "
            "qualquer ação externa. Se o local estiver ausente, pergunte por ele; se estiver "
            "presente, oriente e encerre."
        )
    if decisao.get("acao") not in ACOES_CONVERSACIONAIS:
        raise ValueError("Ação recusada: não pertence ao conjunto conversacional permitido.")
    if not isinstance(decisao.get("mensagem"), str):
        raise ValueError("A mensagem da decisão deve ser texto.")
    if not isinstance(decisao.get("concluiu"), bool):
        raise ValueError("A decisão deve declarar se o ciclo terminou.")
    if not isinstance(decisao.get("motivo"), str):
        raise ValueError("O motivo da decisão deve ser texto.")
    if decisao["acao"] == "perguntar_local" and decisao["concluiu"]:
        raise ValueError("Perguntar o local não pode encerrar o ciclo.")
    if decisao["acao"] == "orientar_e_encerrar" and not decisao["concluiu"]:
        raise ValueError("Orientar neste exemplo precisa encerrar o ciclo.")
    return decisao
