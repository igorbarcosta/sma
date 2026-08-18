# Ambiente de desenvolvimento

O mesmo projeto Python é usado localmente e no GitHub Codespaces. Codespaces é uma alternativa para quem encontrar dificuldades na configuração local, não um requisito da disciplina.

## Ambiente local

Pré-requisitos: Git, Python 3.12 e `uv` 0.11.21.

```bash
git clone <endereço-do-repositório>
cd sma
uv sync --locked
uv run python scripts/check_env.py
```

O endereço será informado quando o repositório remoto existir.

## GitHub Codespaces

1. Abrir o repositório em um Codespace.
2. Aguardar a preparação automática do ambiente.
3. Executar o mesmo diagnóstico:

```bash
uv run python scripts/check_env.py
```

Os encontros futuros deverão usar os mesmos comandos nos dois ambientes. Credenciais e secrets serão documentados somente quando um provider for escolhido; nenhuma chave é necessária para validar o ambiente atual.
