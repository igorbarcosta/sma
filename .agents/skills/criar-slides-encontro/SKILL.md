---
name: criar-slides-encontro
description: Deriva um deck Marp e suas distribuições oficiais de um encontro de SMA cujo roteiro público já esteja pedagogicamente definido e validado. Use quando o usuário pedir slides de um encontro existente; não use para planejar o encontro, decidir currículo ou criar slides sem fonte pedagógica aprovada.
---

# Criar slides do encontro

## Confirmar a fonte

1. Ler `AGENTS.md` e `specs/organizacao-dos-materiais.md`.
2. Ler integralmente a página correspondente em `docs/encontros/`.
3. Confirmar que o roteiro está definido e validado; não preencher lacunas pedagógicas importantes.
4. Consultar retrospectivas relacionadas somente para calibrar o material.
5. Reutilizar `slides/theme/sma.css`; não criar um sistema visual paralelo.

## Derivar o deck

1. Reconstruir a experiência do encontro e preservar o arco narrativo aprovado na página ou no planejamento, com problema, tensões, previsões, investigações, formalizações, aplicações e transferências pertinentes.
2. Fazer cada frame mover a história conceitual por casos, perguntas, revelações, contrastes ou progressão visual; evitar sequências de tópicos independentes.
3. Trabalhar uma ideia principal por frame e manter na página pública as explicações detalhadas.
4. Representar atividades sem revelar antecipadamente suas respostas.
5. Usar apenas categorias visuais genéricas já aprovadas e somente quando tiverem função semântica real.
6. Usar notas do apresentador para orientações que não precisem permanecer projetadas.
7. Criar `slides/encontro-XX-<slug>.md` sem alterar a intenção pedagógica do roteiro.

Não criar uma taxonomia visual nova, escolher tecnologias ou transformar seções mecanicamente em slides.

## Renderizar e validar

1. gerar HTML e PDF em `slides/rendered/` com `npm run slides:render -- encontro-XX-<slug>`;
2. inspecionar visualmente todos os frames;
3. corrigir overflow pela densidade e divisão antes de reduzir fonte;
4. nunca editar HTML ou PDF manualmente;
5. executar `npm run validate`, `git diff --check`, `git diff` e `git status`;
6. relatar fonte, renderizados, inspeção e validações.

Não fazer commit, push ou publicação sem solicitação explícita.
