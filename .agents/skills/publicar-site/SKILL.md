---
name: publicar-site
description: Publica no GitHub Pages o estado local já aprovado de SMA por meio de auditoria, validação, commit consciente, push e promoção segura de `draft` para `main`. Use somente quando o usuário pedir explicitamente para publicar ou atualizar o site online; não use para apenas construir, validar, revisar conteúdo ou interpretar material pronto como autorização de publicação.
---

# Publicar site

Publicar somente mediante autorização explícita. Não usar esta skill para criar ou melhorar conteúdo.

## Auditar o trabalho

1. Ler `AGENTS.md`, `.gitignore`, `pyproject.toml`, `uv.lock`, `package.json` e os workflows.
2. Executar `git status`, `git status --short --untracked-files=all` e `git diff --check`.
3. Inspecionar alterações tracked, staged e não rastreadas e relacionar cada uma ao trabalho aprovado.
4. Procurar temporários, caches, credenciais, segredos e arquivos inesperados.

Diante de item inesperado ou sem relação comprovada, parar. Não remover, descartar, ocultar ou incluir o item. Nunca usar `git add .`, `git clean`, `git reset --hard` ou comandos equivalentes.

## Validar antes do staging

1. Sincronizar dependências somente com `uv sync --locked` e `npm ci`, quando necessário.
2. Executar `npm run validate`.
3. Corrigir apenas falhas técnicas evidentes pertencentes ao escopo aprovado; diante de decisão pedagógica ou estrutural, parar.
4. Repetir status, diff e auditoria depois da validação.

## Confirmar o destino

Identificar por operações de leitura:

- branch atual;
- existência de `draft` e `main`;
- remote `origin` e URLs configuradas;
- relação das branches locais com seus remotes;
- workflow de Pages e URL pública, quando efetivamente configurada.

Exigir que a publicação comece em `draft`. Não criar branch, remote ou URL durante esta skill. Diante de ausência, divergência ou ambiguidade, parar e relatar.

## Commitar conscientemente

1. Selecionar para staging somente os caminhos aprovados, nunca `git add .`.
2. Inspecionar `git diff --staged`, seu resumo e `git diff --staged --check`.
3. Parar se surgir item inesperado.
4. Criar um commit novo com mensagem objetiva; não alterar commits anteriores ou histórico.

## Enviar e promover

1. Enviar `draft` ao `origin` com push normal.
2. Trocar para `main`.
3. Atualizar `main` exclusivamente por fast-forward de `draft`.
4. Enviar `main` ao `origin` com push normal.
5. Nunca usar force push, rebase ou merge commit.

Se qualquer push for rejeitado ou o fast-forward não for possível, não executar pull, merge ou rebase automaticamente. Parar e relatar.

## Verificar e encerrar

1. Consultar o workflow `Documentation` disparado pelo push em `main`, quando `gh` estiver disponível e autenticado.
2. Não modificar o workflow durante a verificação.
3. Confirmar a URL somente pela configuração real do GitHub; nunca inferi-la do nome do repositório.
4. Voltar para `draft`.
5. Executar `git status` e relatar validação, commit, pushes, deploy, URL confirmada e estado final.

Não criar conteúdo, decidir currículo, remover arquivos inesperados, descartar trabalho local ou publicar mudanças que não possam ser relacionadas à autorização recebida.
