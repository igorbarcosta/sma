# Ambiente de desenvolvimento

O mesmo projeto Python é usado localmente e no GitHub Codespaces. Codespaces é uma alternativa para quem encontrar dificuldades na configuração local, não um requisito da disciplina.

## Ambiente local

Pré-requisitos: Git, Python 3.12 e `uv` 0.11.21.

```bash
git clone <endereço-do-repositório>
cd sma
uv sync --locked
cp .env.example .env
# Edite .env e preencha sua chave pessoal.
set -a
source .env
set +a
uv run python scripts/check_env.py
```

Obtenha sua chave pessoal no [Google AI Studio](https://aistudio.google.com/app/apikey). O arquivo `.env` é local e não deve ser versionado ou compartilhado. Para confirmar também autenticação, conectividade e disponibilidade do modelo de referência, execute explicitamente:

```bash
uv run python scripts/check_env.py --check-api
```

O endereço será informado quando o repositório remoto existir.

## GitHub Codespaces

1. Cadastrar `GEMINI_API_KEY` como secret pessoal do Codespaces e permitir seu uso neste repositório.
2. Abrir ou recriar o Codespace.
3. Aguardar a preparação automática do ambiente.
4. Executar o mesmo diagnóstico:

```bash
uv run python scripts/check_env.py
```

O teste opcional de conectividade usa o mesmo comando `--check-api` nos dois ambientes. O diagnóstico comum não chama a API nem consome quota.

Os encontros futuros deverão usar os mesmos comandos nos dois ambientes. Cada estudante é responsável por sua própria credencial; não existe chave compartilhada da turma. Não use dados pessoais, institucionais, confidenciais ou sensíveis nos exercícios. Os materiais oficiais usam somente dados sintéticos ou controlados.
