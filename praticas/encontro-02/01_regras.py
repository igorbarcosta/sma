from __future__ import annotations

import argparse

from suporte import buscar_caso


parser = argparse.ArgumentParser()
parser.add_argument("caso", nargs="?", default="internet-urgente")
args = parser.parse_args()

caso = buscar_caso(args.caso)
estado = caso["estado"]

if estado["categoria"] == "internet" and estado["urgente"]:
    acao = "abrir_chamado_prioritario"
else:
    acao = "abrir_chamado_normal"

print(f"MENSAGEM: {caso['mensagem']}")
print(f"ESTADO: {estado}")
print(f"Ação: {acao}")
