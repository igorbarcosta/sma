"""O sistema de chamados local que o CampusBot pode observar e modificar."""

from __future__ import annotations

from copy import deepcopy
from typing import Any


def criar_ambiente(
    *, chamados_iniciais: list[dict[str, str]] | None = None, servico_disponivel: bool = True
) -> dict[str, Any]:
    """Cria um ambiente sintético e isolado para cada execução."""
    return {
        "chamados": deepcopy(chamados_iniciais or []),
        "servico_disponivel": servico_disponivel,
    }


def buscar_chamados(ambiente: dict[str, Any], local: str) -> list[dict[str, str]]:
    """Lê os chamados daquele local no ambiente."""
    return [chamado for chamado in ambiente["chamados"] if chamado["local"] == local]


def criar_chamado(ambiente: dict[str, Any], local: str, problema: str) -> dict[str, Any]:
    """Modifica o ambiente quando o serviço local está disponível."""
    if not ambiente["servico_disponivel"]:
        return {"ok": False, "erro": "serviço indisponível"}

    protocolo = f"CH-{len(ambiente['chamados']) + 1:03d}"
    chamado = {"protocolo": protocolo, "local": local, "problema": problema}
    ambiente["chamados"].append(chamado)
    return {"ok": True, "protocolo": protocolo}


def retrato(ambiente: dict[str, Any]) -> list[dict[str, str]]:
    """Devolve uma cópia legível do que existe no ambiente agora."""
    return deepcopy(ambiente["chamados"])
