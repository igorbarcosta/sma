from __future__ import annotations

import argparse

from agente import executar_ciclo


parser = argparse.ArgumentParser(description="Executa versões deliberadamente limitadas do ciclo.")
parser.add_argument("caso", nargs="?", default="projetor")
parser.add_argument("--sem-estado", action="store_true", help="não entrega ao decisor o estado atualizado")
parser.add_argument("--limite", type=int, default=4, help="quantidade máxima de passos")
parser.add_argument("--online", action="store_true", help="faz uma chamada real à Gemini API")
args = parser.parse_args()

if args.limite < 1:
    raise SystemExit("ERRO: o limite precisa ser ao menos 1.")

try:
    executar_ciclo(
        args.caso,
        online=args.online,
        manter_estado=not args.sem_estado,
        limite_passos=args.limite,
    )
except (RuntimeError, ValueError) as erro:
    raise SystemExit(f"ERRO: {erro}") from erro
