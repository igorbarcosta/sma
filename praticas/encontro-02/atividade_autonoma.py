"""Starter da missão autônoma: substitua o caso e simplifique a arquitetura."""

from suporte import executar_acao


mensagem = "A sala está sem projetor, mas talvez exista outro disponível."

# MINHA HIPÓTESE
#
# Arquitetura escolhida:
#
# Por que ela é suficiente:
#
# Por que não escolhi algo mais complexo:
#
# O que aconteceu quando executei:
#
# Para transformar esta solução em um agente mais completo, acho que seriam necessários:

# Comece com uma hipótese simples. Troque esta decisão por regra, workflow,
# extração com LLM ou decisão dinâmica somente se o seu requisito precisar.
if "sem projetor" in mensagem.casefold():
    acao = "encaminhar_para_humano"
else:
    acao = "pedir_informacao"

print(f"Solicitação sintética: {mensagem}")
print(f"Arquitetura escolhida: regra")
print(f"Ação: {acao}")
executar_acao(acao)
