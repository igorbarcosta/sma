from __future__ import annotations

import argparse

from ambiente import criar_ambiente
from controlador import executar_ciclo


PEDIDO = "O projetor do Lab 4 não funciona. Veja se já existe um chamado. Se não existir, abra um."
CHAMADO_EXISTENTE = {"protocolo": "CH-001", "local": "Lab 4", "problema": "projetor não funciona"}
parser = argparse.ArgumentParser(description="Executa o CampusBot com duas ferramentas explícitas.")
parser.add_argument("--offline", action="store_true", help="usa decisões simuladas e reproduzíveis")
parser.add_argument("--com-chamado-existente", action="store_true", help="pré-carrega CH-001 no Lab 4")
parser.add_argument("--resultado-nao-volta", action="store_true", help="executa sem devolver resultado à decisão seguinte")
args = parser.parse_args()

ambiente = criar_ambiente(chamados_iniciais=[CHAMADO_EXISTENTE] if args.com_chamado_existente else [])
try:
    executar_ciclo(PEDIDO, ambiente, offline=args.offline, devolver_resultado=not args.resultado_nao_volta)
except (RuntimeError, ValueError, KeyError) as erro:
    raise SystemExit(f"ERRO: {erro}") from erro
