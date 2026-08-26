from __future__ import annotations

from llm import decidir
from suporte import executar_acao


objetivo = "Dar a orientação conhecida para um objeto perdido quando o local é conhecido."
estado = {"categoria": "objeto_perdido", "urgente": False, "local": "Lab 3"}

# O sistema começa com decisão dinâmica. Sua missão é substituí-la pela menor
# arquitetura suficiente sem alterar o requisito nem a consequência observada.
decisao = decidir(objetivo, estado, online=False)
acao = decisao["acao"]

print(f"DECISÃO INICIAL: {decisao}")
executar_acao(acao)
