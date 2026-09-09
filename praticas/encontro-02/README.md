# Encontro 02 — Quando vale a pena tornar um sistema agentivo?

## Comece por

Execute a partir da raiz do repositório:

```bash
uv run python praticas/encontro-02/01_regras.py
```

## Ordem da experiência

1. `01_regras.py` — entrada estruturada e regra;
2. `02_workflow_com_llm.py` — linguagem natural extraída por LLM;
3. `03_workflow_crescendo.py` — mais requisitos em um fluxo explícito;
4. `04_decisao_dinamica.py` — escolha estruturada em execução;
5. `mate_o_agente.py` — simplificação deliberada da arquitetura;
6. `atividade_autonoma.py` — starter para transferência.

Todos os dados são sintéticos. Os exemplos com LLM chamam por padrão o modelo
definido em `config/llm.toml` e exigem `GEMINI_API_KEY`. O terminal mostra
`MODO ONLINE — GEMINI`. A opção `--offline` usa uma resposta simulada e mostra
`MODO OFFLINE — RESPOSTA SIMULADA`.

Comandos seguintes:

```bash
uv run python praticas/encontro-02/02_workflow_com_llm.py
uv run python praticas/encontro-02/03_workflow_crescendo.py
uv run python praticas/encontro-02/04_decisao_dinamica.py
uv run python praticas/encontro-02/mate_o_agente.py
uv run python praticas/encontro-02/atividade_autonoma.py
```

Para executar o modo padrão, configure `GEMINI_API_KEY` como secret pessoal no
Codespaces e permita seu uso neste repositório. Se ele já estiver aberto,
reinicie o Codespace para receber o secret. Não coloque a chave no código nem em
arquivos do projeto.

Se precisar executar sem chave ou sem internet, use a alternativa offline:

```bash
uv run python praticas/encontro-02/02_workflow_com_llm.py --offline
uv run python praticas/encontro-02/04_decisao_dinamica.py --offline
```
