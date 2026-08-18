---
name: criar-encontro
description: Cria ou atualiza o roteiro público de um encontro de SMA a partir de um desenho pedagógico já decidido e validado. Use quando o usuário pedir para implementar um encontro específico em `docs/encontros/`; não use para decidir a macroprogressão, inventar atividades, criar os 14 encontros antecipadamente ou derivar slides.
---

# Criar encontro

## Preparar

1. Ler `AGENTS.md`.
2. Ler `specs/projeto-pedagogico.md` e `specs/organizacao-dos-materiais.md` integralmente.
3. Ler `specs/avaliacao-e-uso-de-ia.md` quando o encontro se relacionar a uma avaliação, desafio ou projeto.
4. Consultar retrospectivas relevantes da oferta como evidência contextual, nunca como regra.
5. Confirmar que o pedido define suficientemente problema, resultados pretendidos, escopo e operações cognitivas. Diante de decisão pedagógica importante ausente, pedir orientação.

## Implementar

1. Criar ou atualizar `docs/encontros/encontro-XX-<slug>.md`.
2. Preservar a trajetória causal do desenho aprovado, partindo do problema antes da formalização.
3. Explicitar no planejamento de cada atividade a operação cognitiva e sua evidência observável.
4. Dimensionar o encontro sem tratá-lo como exposição de 200 minutos e sem impor `Aula → Laboratório`.
5. Usar scaffolding e autonomia conforme definidos no desenho do encontro.
6. Manter no material público apenas informações úteis ao estudante.

Não escolher frameworks, bibliotecas, stack, bibliografia, datas, prazos ou critérios não fornecidos. Não criar slides nesta skill.

## Validar

1. Verificar coerência com a macroprogressão e com os encontros adjacentes existentes.
2. Confirmar que IA, quando envolvida, segue a política aprovada.
3. Executar as validações disponíveis, `git diff --check`, `git diff` e `git status`.
4. Relatar arquivos alterados, trajetória, operações cognitivas e validações.

Não fazer commit, push ou publicação sem solicitação explícita.
