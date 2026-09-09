from __future__ import annotations

from copy import deepcopy
from typing import Any


CASOS: dict[str, dict[str, Any]] = {
    "projetor": {
        "objetivo": "Ajudar a pessoa com um problema de projetor sem inventar uma ação externa.",
        "mensagem_inicial": "O projetor não funciona e a apresentação começa em breve.",
        "respostas": ["É no Lab 4."],
        "estado_inicial": {"local": None, "problema": "projetor", "urgente": True},
    },
    "acesso": {
        "objetivo": "Ajudar a pessoa com acesso bloqueado sem inventar uma ação externa.",
        "mensagem_inicial": "Não consigo entrar no sistema de reservas.",
        "respostas": ["Acontece no laboratório de redes."],
        "estado_inicial": {"local": None, "problema": "acesso", "urgente": False},
    },
}


def buscar_caso(identificador: str) -> dict[str, Any]:
    try:
        return deepcopy(CASOS[identificador])
    except KeyError as erro:
        disponiveis = ", ".join(CASOS)
        raise ValueError(f"Caso desconhecido. Use um destes: {disponiveis}") from erro
