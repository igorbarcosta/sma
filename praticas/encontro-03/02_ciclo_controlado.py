from __future__ import annotations

import argparse

from agente import executar_ciclo


parser = argparse.ArgumentParser(description="Executa o ciclo conversacional controlado do CampusBot.")
parser.add_argument("caso", nargs="?", default="projetor")
parser.add_argument("--online", action="store_true", help="faz uma chamada real à Gemini API")
args = parser.parse_args()

try:
    executar_ciclo(args.caso, online=args.online)
except (RuntimeError, ValueError) as erro:
    raise SystemExit(f"ERRO: {erro}") from erro
