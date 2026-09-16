"""Atividade formativa: acrescente uma única ferramenta ao CampusBot."""

from __future__ import annotations

import argparse

from ambiente import criar_ambiente
from controlador import executar_ciclo


# MISSÃO
#
# Adicione consultar_status(protocolo) ao mesmo sistema, sem criar outra arquitetura.
# Ela deve consultar no ambiente um chamado já existente e devolver, por exemplo:
# {"ok": True, "protocolo": "CH-001", "status": "aberto"}
#
# Faça mudanças pequenas e visíveis:
# 1. crie a função em ferramentas.py (e a leitura necessária em ambiente.py);
# 2. acrescente a escolha no contrato de modelo.py e na política offline;
# 3. acrescente um `if` explícito em controlador.py que a execute.
#
# Produza uma execução em que apareçam, nesta ordem:
# decisão → solicitação → execução → resultado → decisão seguinte.
# Depois responda no seu registro:
# - Qual ferramenta foi solicitada?
# - Quem a executou de fato?
# - O que ela consultou ou modificou no ambiente?
# - Qual resultado chegou ao modelo?
# - Como esse resultado mudou a próxima decisão?

parser = argparse.ArgumentParser(description="Executa o ponto de partida da atividade autônoma.")
parser.add_argument("--offline", action="store_true", help="usa decisões simuladas e reproduzíveis")
args = parser.parse_args()

ambiente = criar_ambiente(chamados_iniciais=[{"protocolo": "CH-001", "local": "Lab 4", "problema": "projetor não funciona"}])
try:
    executar_ciclo("Veja se já existe um chamado para o projetor do Lab 4. Se não existir, abra um.", ambiente, offline=args.offline)
except (RuntimeError, ValueError, KeyError) as erro:
    raise SystemExit(f"ERRO: {erro}") from erro
