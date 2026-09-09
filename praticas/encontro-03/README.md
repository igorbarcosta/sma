# Encontro 03 — Do que é feito um agente baseado em LLM?

Execute os programas a partir da raiz do repositório:

```bash
uv run python praticas/encontro-03/01_uma_resposta.py
uv run python praticas/encontro-03/02_ciclo_controlado.py
uv run python praticas/encontro-03/03_diagnosticar_o_ciclo.py --sem-estado
uv run python praticas/encontro-03/atividade_autonoma.py
```

A prática funciona sem chave e sem internet. Nessa modalidade, o arquivo
`modelo.py` usa uma decisão simulada e anuncia isso no terminal. Para substituir
somente a decisão simulada por uma chamada real ao modelo configurado em
`config/llm.toml`, use `--online` em `02_ciclo_controlado.py` ou
`03_diagnosticar_o_ciclo.py`:

```bash
uv run python praticas/encontro-03/02_ciclo_controlado.py --online
```

Isso exige que `GEMINI_API_KEY` esteja disponível no ambiente. A chave nunca é
gravada nem exibida pela prática.

O agente desta experiência só conversa com uma pessoa simulada. Ele não consulta
sistemas, não abre chamados e não altera recursos externos. A próxima etapa da
disciplina investigará o que muda quando o agente ganha ferramentas para agir no
ambiente.
