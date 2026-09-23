"""Informação mantida pelo sistema enquanto esta execução está ativa."""

from copy import deepcopy


def criar_estado():
    return {
        "usuario": "docente", "local": "Lab 4", "problema": "projetor não funciona",
        "urgente": False, "ultima_consulta": None, "ultima_abertura": None,
        "historico_chamados": [], "logs": ["início da execução"],
        "preferencias": {"idioma": "pt-BR"},
    }


def atualizar_estado(estado, ferramenta, resultado):
    """Conserva um resultado para uma decisão posterior."""
    if ferramenta == "consultar_chamados":
        estado["ultima_consulta"] = deepcopy(resultado)
        estado["historico_chamados"] = deepcopy(resultado["chamados"])
    elif ferramenta == "abrir_chamado":
        estado["ultima_abertura"] = deepcopy(resultado)
    estado["logs"].append(f"{ferramenta} executada")
