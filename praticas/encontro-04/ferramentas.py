"""Capacidades que o programa pode executar no ambiente de chamados."""

from __future__ import annotations

from typing import Any

from ambiente import buscar_chamados, criar_chamado


def consultar_chamados(ambiente: dict[str, Any], local: str) -> dict[str, Any]:
    """Consulta, mas não altera, o ambiente."""
    chamados = buscar_chamados(ambiente, local)
    return {"ok": True, "chamados": chamados}


def abrir_chamado(ambiente: dict[str, Any], local: str, problema: str) -> dict[str, Any]:
    """Pede ao ambiente que registre um chamado."""
    return criar_chamado(ambiente, local, problema)
