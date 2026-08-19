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
2. Representar no deck todas as ideias conceitualmente importantes da página — exemplos, contraexemplos, comparações, perguntas, análises, exemplos trabalhados, sínteses e transições — sem copiar mecanicamente seus parágrafos.
3. Fazer cada frame mover a história conceitual por casos, perguntas, revelações, contrastes ou progressão visual; evitar sequências de tópicos independentes.
4. Trabalhar uma ideia principal por frame e obter minimalismo reduzindo densidade, não removendo conteúdo nem perseguindo uma quantidade pequena de slides.
5. Representar atividades e perguntas sem revelar antecipadamente suas respostas; depois da investigação, incluir a resposta, análise ou possível interpretação no próprio deck.
6. Garantir que HTML e PDF permitam ao estudante reconstruir posteriormente o percurso conceitual sem depender das notas do apresentador.
7. Usar apenas categorias visuais genéricas já aprovadas e somente quando tiverem função semântica real.
8. Usar notas do apresentador apenas para timing, votação, espera, condução e erros esperados; conteúdo conceitual necessário deve aparecer em algum frame.
9. Criar `slides/encontro-XX-<slug>.md` sem alterar a intenção pedagógica do roteiro.

Não criar uma taxonomia visual nova, escolher tecnologias ou transformar seções mecanicamente em slides.

## Renderizar e validar

1. gerar HTML e PDF em `slides/rendered/` com `npm run slides:render -- encontro-XX-<slug>`;
2. construir uma matriz interna `seção da página → frames` e confirmar que nenhuma ideia foi omitida apenas para reduzir o número de slides;
3. auditar toda pergunta conceitual, verificando se sua análise aparece depois — nunca antes ou apenas nas notas;
4. inspecionar visualmente todos os frames e confirmar narrativa, contraste, legibilidade a distância e compreensão posterior em HTML/PDF;
5. corrigir overflow pela densidade e divisão antes de reduzir fonte;
6. nunca editar HTML ou PDF manualmente;
7. executar `npm run validate`, `git diff --check`, `git diff` e `git status`;
8. relatar fonte, renderizados, cobertura conceitual, perguntas/respostas, inspeção e validações.

Não fazer commit, push ou publicação sem solicitação explícita.
