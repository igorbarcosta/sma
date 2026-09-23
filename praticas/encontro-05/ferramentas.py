"""As duas capacidades do CampusBot, mantidas do Encontro 04."""

from ambiente import retrato


def consultar_chamados(ambiente, local):
    return {"ok": True, "chamados": [c for c in retrato(ambiente) if c["local"] == local]}


def abrir_chamado(ambiente, local, problema):
    numero = max((int(c["protocolo"][3:]) for c in ambiente["chamados"]), default=0) + 1
    protocolo = f"CH-{numero:03d}"
    ambiente["chamados"].append({"protocolo": protocolo, "local": local, "problema": problema, "status": "aberto"})
    return {"ok": True, "protocolo": protocolo}
