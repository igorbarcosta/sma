from __future__ import annotations

import argparse

from modelo import responder_sem_agir


PEDIDO = "O projetor do Lab 4 não funciona. Abra um chamado."
parser = argparse.ArgumentParser(description="Mostra uma resposta sem consequência no ambiente.")
parser.add_argument("--offline", action="store_true", help="usa uma resposta simulada")
args = parser.parse_args()

print(f"[USUÁRIO]\n{PEDIDO}")
try:
    resposta = responder_sem_agir(PEDIDO, args.offline)
except (RuntimeError, ValueError) as erro:
    raise SystemExit(f"ERRO: {erro}") from erro
print(f"\n[MODELO]\n{resposta}")
print("\n[OBSERVAÇÃO]\nNenhum ambiente foi consultado ou modificado.")
