from __future__ import annotations

import argparse

from ambiente import criar_ambiente
from controlador import executar_ciclo


PEDIDO = "O projetor do Lab 4 não funciona. Abra um chamado."
parser = argparse.ArgumentParser(description="Mostra que pedir, executar e conseguir são coisas diferentes.")
parser.add_argument("--offline", action="store_true", help="usa decisões simuladas e reproduzíveis")
args = parser.parse_args()

try:
    executar_ciclo(PEDIDO, criar_ambiente(servico_disponivel=False), offline=args.offline)
except (RuntimeError, ValueError, KeyError) as erro:
    raise SystemExit(f"ERRO: {erro}") from erro
