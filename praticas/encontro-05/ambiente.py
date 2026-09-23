"""Chamados sintéticos; a realidade do ambiente é separada do que o agente sabe."""

from copy import deepcopy


def criar_ambiente(chamados=None):
    return {"chamados": deepcopy(chamados or [])}


def retrato(ambiente):
    return deepcopy(ambiente["chamados"])
