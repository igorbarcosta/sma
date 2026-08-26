from __future__ import annotations

import argparse
import json

from llm import decidir
from suporte import buscar_caso, executar_acao


parser = argparse.ArgumentParser()
parser.add_argument("caso", nargs="?", default="internet-urgente")
parser.add_argument("--online", action="store_true", help="faz uma chamada real à Gemini API")
args = parser.parse_args()

caso = buscar_caso(args.caso)
objetivo = "Ajudar a resolver a solicitação usando somente ações permitidas."
try:
    decisao = decidir(objetivo, caso["estado"], online=args.online)
except RuntimeError as erro:
    raise SystemExit(f"ERRO: {erro}") from erro

print(f"OBJETIVO: {objetivo}")
print("ESTADO:", json.dumps(caso["estado"], ensure_ascii=False))
print("AÇÕES: pedir informação, abrir chamado, orientar, encaminhar ou encerrar")
print("DECISÃO:", json.dumps(decisao, ensure_ascii=False))
executar_acao(decisao["acao"])
