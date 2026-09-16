# Encontro 04 — Como um agente passa de responder para agir?

Execute a partir da raiz do repositório. Comece em modo offline para uma execução reproduzível:

```bash
uv run python praticas/encontro-04/01_so_responde.py --offline
uv run python praticas/encontro-04/02_primeira_ferramenta.py
uv run python praticas/encontro-04/03_agente_com_ferramentas.py --offline
uv run python praticas/encontro-04/04_quando_a_ferramenta_falha.py --offline
```

Na demonstração principal, o modo offline anuncia `MODO OFFLINE — DECISÃO SIMULADA`. Ele reproduz de forma transparente a decisão que uma LLM tomaria; não é uma chamada ao Gemini. Sem `--offline`, os programas que usam modelo anunciam `MODO ONLINE — GEMINI`, usam o provider e o modelo definidos em `config/llm.toml` e exigem uma `GEMINI_API_KEY` pessoal. A chave nunca é gravada ou exibida.

Experimentos controlados:

```bash
# O ambiente já possui CH-001: consultar deve evitar uma abertura duplicada.
uv run python praticas/encontro-04/03_agente_com_ferramentas.py --com-chamado-existente --offline

# A ferramenta executa, mas o modelo não observa seu resultado e repete a consulta.
uv run python praticas/encontro-04/03_agente_com_ferramentas.py --com-chamado-existente --resultado-nao-volta --offline

# A abertura falha: a resposta seguinte deve reconhecer a falha, não inventar sucesso.
uv run python praticas/encontro-04/04_quando_a_ferramenta_falha.py --offline
```

Os quatro arquivos de responsabilidade são intencionais:

```text
modelo.py       decide responder ou solicitar uma ferramenta
controlador.py  recebe a decisão, executa e devolve o resultado
ferramentas.py  representa capacidades executáveis
ambiente.py     guarda o sistema de chamados local em memória
```

Leia `atividade_autonoma.py` para a missão formativa: adicionar uma única ferramenta de consulta de status e registrar a cadeia de evidências, não apenas o fato de o código funcionar.
