"""Recortes explícitos do estado entregues ao mesmo decisor."""

from copy import deepcopy


def montar_contexto(estado, modo="adequado"):
    """Altere esta função na intervenção 1; compare antes e depois."""
    if modo == "demais":
        return deepcopy(estado)
    contexto = {"local": estado["local"], "problema": estado["problema"]}
    if modo in {"adequado", "memoria"}:
        contexto["ultima_consulta"] = deepcopy(estado["ultima_consulta"])
        contexto["ultima_abertura"] = deepcopy(estado["ultima_abertura"])
    if modo == "memoria":
        contexto["memoria"] = deepcopy(estado.get("memoria"))
    return contexto
