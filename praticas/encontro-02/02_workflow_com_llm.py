from __future__ import annotations

import argparse
import json

from llm import interpretar
from suporte import carregar_casos, encaminhar_por_regras, executar_acao


parser = argparse.ArgumentParser()
parser.add_argument(
    "entrada",
    nargs="?",
    default="O Wi-Fi morreu no laboratório e minha apresentação começa daqui a pouco.",
    help="identificador de casos.json ou mensagem livre",
)
parser.add_argument("--offline", action="store_true", help="usa uma resposta simulada, sem chamar a Gemini API")
args = parser.parse_args()

casos_por_id = {caso["id"]: caso for caso in carregar_casos()}
mensagem = casos_por_id.get(args.entrada, {}).get("mensagem", args.entrada)

try:
    estado = interpretar(mensagem, offline=args.offline)
except RuntimeError as erro:
    raise SystemExit(f"ERRO: {erro}") from erro
acao = encaminhar_por_regras(estado)

print("ESTRUTURA:", json.dumps(estado, ensure_ascii=False))
print(f"REGRA ESCOLHEU: {acao}")
executar_acao(acao)
