from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PASTA = Path(__file__).resolve().parent
ACOES_PERMITIDAS = {
    "pedir_informacao",
    "abrir_chamado_normal",
    "abrir_chamado_prioritario",
    "fornecer_orientacao",
    "encaminhar_para_humano",
    "encerrar",
}


def carregar_casos() -> list[dict[str, Any]]:
    return json.loads((PASTA / "casos.json").read_text(encoding="utf-8"))


def buscar_caso(identificador: str) -> dict[str, Any]:
    for caso in carregar_casos():
        if caso["id"] == identificador:
            return caso
    disponiveis = ", ".join(caso["id"] for caso in carregar_casos())
    raise ValueError(f"Caso desconhecido. Use um destes: {disponiveis}")


def encaminhar_por_regras(estado: dict[str, Any]) -> str:
    if not estado.get("local"):
        return "pedir_informacao"
    if estado.get("categoria") == "internet" and estado.get("urgente"):
        return "abrir_chamado_prioritario"
    if estado.get("categoria") in {"internet", "computador", "climatizacao"}:
        return "abrir_chamado_normal"
    if estado.get("categoria") == "objeto_perdido":
        return "fornecer_orientacao"
    return "encaminhar_para_humano"


def executar_acao(acao: str) -> None:
    if acao not in ACOES_PERMITIDAS:
        raise ValueError(f"Ação recusada: {acao!r} não está entre as ações permitidas.")
    consequencias = {
        "pedir_informacao": "CampusBot pergunta em qual local ocorreu o problema.",
        "abrir_chamado_normal": "Chamado normal simulado foi registrado.",
        "abrir_chamado_prioritario": "Chamado prioritário simulado foi registrado.",
        "fornecer_orientacao": "CampusBot mostra uma orientação conhecida.",
        "encaminhar_para_humano": "Solicitação simulada foi encaminhada a uma pessoa.",
        "encerrar": "Solicitação encerrada sem nova ação.",
    }
    print(f"CONSEQUÊNCIA: {consequencias[acao]}")
