"""O componente que escolhe responder ou solicitar uma ferramenta."""

from __future__ import annotations

import json
import os
import tomllib
from pathlib import Path
from typing import Any


RAIZ = Path(__file__).resolve().parents[2]
CONFIGURACAO = RAIZ / "config" / "llm.toml"
FERRAMENTAS_DISPONIVEIS = {"consultar_chamados", "abrir_chamado"}


def _modelo_configurado() -> str:
    with CONFIGURACAO.open("rb") as arquivo:
        configuracao = tomllib.load(arquivo)
    if configuracao.get("provider") != "gemini":
        raise ValueError("Esta prática espera o provider gemini em config/llm.toml.")
    return str(configuracao["model"])


def _gerar_texto(prompt: str) -> str:
    chave = os.environ.get("GEMINI_API_KEY")
    if not chave:
        raise RuntimeError("Defina GEMINI_API_KEY ou execute com --offline.")
    from google import genai
    cliente = genai.Client(api_key=chave)
    try:
        resposta = cliente.models.generate_content(model=_modelo_configurado(), contents=prompt)
    finally:
        cliente.close()
    if not resposta.text:
        raise RuntimeError("O modelo não devolveu conteúdo.")
    return resposta.text


def responder_sem_agir(pedido: str, offline: bool) -> str:
    """Mostra uma resposta textual sem dar ao programa uma consequência externa."""
    print("MODO OFFLINE — RESPOSTA SIMULADA" if offline else "MODO ONLINE — GEMINI")
    if offline:
        return "Eu abriria um chamado para o projetor do Lab 4. (Resposta simulada; nenhum chamado foi aberto.)"
    return _gerar_texto(
        "Você é o CampusBot. Responda em uma frase curta ao pedido abaixo. "
        "Você não tem acesso ao sistema de chamados: não afirme que executou uma ação.\n"
        f"Pedido: {pedido}"
    )


def _decisao_simulada(pedido: str, observacoes: list[dict[str, Any]]) -> dict[str, Any]:
    """Política reproduzível: consulta antes de abrir quando o pedido exige isso."""
    resultados = {item["ferramenta"]: item["resultado"] for item in observacoes}
    abertura = resultados.get("abrir_chamado")
    consulta = resultados.get("consultar_chamados")
    if abertura:
        if abertura["ok"]:
            return {"tipo": "responder", "mensagem": f"O chamado {abertura['protocolo']} foi aberto."}
        return {"tipo": "responder", "mensagem": f"Não consegui abrir o chamado: {abertura['erro']}."}
    if "veja se" in pedido.lower() and consulta is not None:
        if consulta["chamados"]:
            protocolo = consulta["chamados"][0]["protocolo"]
            return {"tipo": "responder", "mensagem": f"Já existe o chamado {protocolo}."}
        return {
            "tipo": "usar_ferramenta",
            "ferramenta": "abrir_chamado",
            "argumentos": {"local": "Lab 4", "problema": "projetor não funciona"},
        }
    if "veja se" in pedido.lower():
        return {"tipo": "usar_ferramenta", "ferramenta": "consultar_chamados", "argumentos": {"local": "Lab 4"}}
    return {
        "tipo": "usar_ferramenta",
        "ferramenta": "abrir_chamado",
        "argumentos": {"local": "Lab 4", "problema": "projetor não funciona"},
    }


def _gerar_decisao(pedido: str, observacoes: list[dict[str, Any]]) -> dict[str, Any]:
    chave = os.environ.get("GEMINI_API_KEY")
    if not chave:
        raise RuntimeError("Defina GEMINI_API_KEY ou execute com --offline.")
    from google import genai
    from google.genai import types
    cliente = genai.Client(api_key=chave)
    try:
        resposta = cliente.models.generate_content(
            model=_modelo_configurado(),
            contents=(
                "Você é o componente de decisão do CampusBot. Escolha somente o próximo passo.\n"
                f"Pedido da pessoa: {pedido}\n"
                f"Resultados observados: {json.dumps(observacoes, ensure_ascii=False)}\n"
                "Ferramentas: consultar_chamados(local) lista chamados; abrir_chamado(local, problema) tenta registrar.\n"
                "Se o pedido disser para verificar antes, consulte antes de abrir. Se encontrar chamado, responda sem abrir outro. "
                "Só diga que abriu se o resultado tiver ok=true; se falhar, reconheça a falha."
            ),
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_json_schema={
                    "type": "object",
                    "properties": {
                        "tipo": {"type": "string", "enum": ["usar_ferramenta", "responder"]},
                        "ferramenta": {"type": "string"},
                        "argumentos": {"type": "object"},
                        "mensagem": {"type": "string"},
                    },
                    "required": ["tipo"],
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


def validar_decisao(decisao: dict[str, Any]) -> dict[str, Any]:
    """Mantém o contrato pequeno antes de o controlador executar algo."""
    if not isinstance(decisao, dict):
        raise ValueError("A decisão precisa ser um objeto.")
    if decisao.get("tipo") == "responder" and isinstance(decisao.get("mensagem"), str):
        return decisao
    if decisao.get("tipo") == "usar_ferramenta" and decisao.get("ferramenta") in FERRAMENTAS_DISPONIVEIS and isinstance(decisao.get("argumentos"), dict):
        return decisao
    raise ValueError("Decisão recusada: use responder ou uma ferramenta disponível com argumentos.")


def decidir(pedido: str, observacoes: list[dict[str, Any]], offline: bool) -> dict[str, Any]:
    """Decide; não consulta nem modifica o ambiente."""
    print("MODO OFFLINE — DECISÃO SIMULADA" if offline else "MODO ONLINE — GEMINI")
    decisao = _decisao_simulada(pedido, observacoes) if offline else _gerar_decisao(pedido, observacoes)
    return validar_decisao(decisao)
