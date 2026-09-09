# Sistemas Multiagentes / Agentic AI

Este repositório contém os materiais da disciplina de Sistemas Multiagentes / Agentic AI para Engenharia de Computação.

## Autoridade das camadas

- `AGENTS.md`: regras operacionais e limites de autoridade dos agentes.
- `specs/`: decisões pedagógicas e curriculares duráveis; consultar antes de criar ou reorganizar materiais.
- `retrospectivas/`: evidências contextuais da oferta real; não constituem regras permanentes.
- `.agents/skills/`: procedimentos repetíveis para tarefas recorrentes.
- o prompt atual: somente o delta da tarefa em execução.

Em caso de tensão, preservar a distinção: uma retrospectiva descreve o que aconteceu; uma spec registra o que foi decidido como durável. Uma observação isolada não deve ser promovida automaticamente a regra.

## Contexto e estrutura

- O conteúdo público permanente será organizado em `docs/` e escrito preferencialmente em Markdown.
- Encontros usarão futuramente `docs/encontros/encontro-XX-<slug>.md`.
- Desafios práticos, projeto integrador e materiais terão seções públicas próprias.
- O Google Classroom será usado para entregas, prazos, comunicação e notas; não duplicar esses dados operacionais no conteúdo permanente sem necessidade.
- O acervo histórico de fontes Marp em `slides/` e suas distribuições versionadas será preservado; não criar novos slides nem depender deles nos encontros futuros.
- A saída local gerada do site ficará em `site/` e nunca deverá ser editada manualmente.
- O site é construído com Zensical por meio dos scripts documentados no repositório.
- A infraestrutura Marp existente atende apenas ao acervo histórico; não é parte do fluxo de criação de novos encontros.
- Os workflows em `.github/workflows/` validam o repositório e preparam a publicação no GitHub Pages.
- O ambiente Python é gerenciado exclusivamente por `uv`, com `pyproject.toml` e `uv.lock` versionados.
- Python 3.12 é a versão-base; ambiente local e GitHub Codespaces devem usar o mesmo projeto e os mesmos comandos.
- O provider didático padrão inicial é Gemini, com configuração operacional centralizada em `config/llm.toml` e credencial pessoal em `GEMINI_API_KEY`.

## Fontes pedagógicas

Antes de criar ou revisar conteúdo, consultar as specs pertinentes:

- `specs/projeto-pedagogico.md`: identidade, resultados, princípios e macroprogressão;
- `specs/organizacao-dos-materiais.md`: organização temporal, encontros, roteiros e práticas;
- `specs/avaliacao-e-uso-de-ia.md`: instrumentos, pesos e política de IA;
- `specs/retrospectivas.md`: registro e uso de evidências da oferta.

O roteiro pedagógico validado orienta um roteiro público autoguiado e sua prática correspondente. Não criar slides para novos encontros.

## Princípios operacionais

- Priorizar soluções simples, explícitas e fáceis de manter.
- Usar Markdown e recursos nativos das ferramentas quando possível.
- Não adicionar dependências, frameworks ou infraestrutura sem necessidade e decisão explícita.
- Nunca registrar, imprimir ou compartilhar credenciais; arquivos `.env` locais não são versionados.
- Não inventar datas, prazos, bibliografia, avaliações, regras acadêmicas ou decisões curriculares.
- Não escolher framework agentivo, biblioteca principal, gerenciador de ambiente ou stack sem decisão explícita.
- Implementar decisões pedagógicas já aprovadas, mas não tomar decisões pedagógicas importantes no lugar do professor.
- Consultar retrospectivas relevantes para calibrar materiais, sem tratá-las como autoridade normativa.
- Não excluir ou reorganizar conteúdo sem necessidade e autorização.
- Preservar alterações preexistentes e limitar mudanças ao escopo solicitado.

## Branches e publicação

- `draft` é a branch normal de trabalho e revisão.
- `main` representa conteúdo aprovado e publicado.
- Não fazer commit, push ou publicação sem solicitação explícita.
- Não enviar alterações diretamente a `main` como fluxo normal de trabalho.
- A promoção de `draft` para `main` deverá seguir o processo seguro documentado pela futura skill de publicação.
- Nunca usar force push, rebase automático, merge commit de promoção, `git reset --hard` ou descarte de arquivos inesperados.
- Diante de divergência, arquivo inesperado, segredo ou alteração sem relação comprovada com o trabalho, interromper e pedir orientação.

## Verificação

Após alterações:

1. executar as validações disponíveis e pertinentes;
2. executar `git diff --check`;
3. inspecionar `git diff` e `git status`;
4. confirmar que nenhum artefato ou decisão fora do escopo foi introduzido;
5. informar arquivos alterados e validações executadas.

Preparar o ambiente com `uv sync --locked` e diagnosticá-lo com `uv run python scripts/check_env.py`. Os comandos locais oficiais para materiais atuais são `npm run site:build` e `npm run validate`; comandos Marp existem apenas para manutenção excepcional do acervo histórico.

## Regra principal

Começar pela solução mais simples adequada ao problema e introduzir LLM, workflow, agência ou múltiplos agentes somente quando houver justificativa arquitetural sustentada por evidências.
