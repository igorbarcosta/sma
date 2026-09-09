"""Starter formativo: complete a hipótese antes de alterar o programa."""

import argparse

from agente import executar_ciclo


# MINHA HIPÓTESE
#
# Caso escolhido: projetor ou acesso
# Objetivo do agente:
# Percepção inicial:
# Estado que precisa ser preservado durante o ciclo:
# Contexto de decisão neste passo (instruções, objetivo, percepção, estado e ações permitidas):
# Próximo passo que o agente pode escolher:
# Condição de parada:
# Limite que continua existindo sem ferramentas:
#
# Depois de preencher, execute os dois casos e compare o que muda e o que
# permanece na arquitetura:
# uv run python praticas/encontro-03/atividade_autonoma.py projetor --offline
# uv run python praticas/encontro-03/atividade_autonoma.py acesso --offline
#
# Em seguida, execute uma versão limitada e uma decisão inválida:
# uv run python praticas/encontro-03/03_diagnosticar_o_ciclo.py --sem-estado --offline
# uv run python praticas/encontro-03/04_validar_decisao.py
#
# O componente que falhou foi:
# A evidência no terminal foi:
# A mudança mínima que eu faria seria:

parser = argparse.ArgumentParser(description="Executa o ciclo usado na atividade autônoma.")
parser.add_argument("caso", nargs="?", choices=("projetor", "acesso"), default="projetor")
parser.add_argument("--offline", action="store_true", help="usa a decisão simulada para uma comparação reproduzível")
args = parser.parse_args()

executar_ciclo(args.caso, offline=args.offline)
