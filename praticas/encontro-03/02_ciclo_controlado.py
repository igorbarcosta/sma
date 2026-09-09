from __future__ import annotations

import argparse

from agente import executar_ciclo


parser = argparse.ArgumentParser(description="Executa o ciclo conversacional controlado do CampusBot.")
parser.add_argument("caso", nargs="?", default="projetor")
parser.add_argument("--offline", action="store_true", help="usa uma decisão simulada, sem chamar a Gemini API")
args = parser.parse_args()

try:
    executar_ciclo(args.caso, offline=args.offline)
except (RuntimeError, ValueError) as erro:
    raise SystemExit(f"ERRO: {erro}") from erro
