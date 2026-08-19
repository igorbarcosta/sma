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
2. Contar uma história conceitual coerente e causal, preservando, sem impor uma fórmula rígida, a trajetória `problema → tensão → investigação → conceito → aplicação → transferência` do desenho aprovado.
3. Ensinar pelo texto: a página deve ser utilizável sem o professor presente e conter explicações suficientes para aprendizagem, revisão e retomada posterior.
4. Preferir exemplos recorrentes que carreguem a narrativa; desenvolver exemplos trabalhados, comparações e contraexemplos quando contribuírem para a compreensão.
5. Apresentar perguntas antes da explicação quando a investigação for pedagogicamente útil e oferecer análises ou possíveis respostas recolhíveis que expliquem o raciocínio.
6. Usar operação cognitiva e evidência observável para planejar e validar cada atividade, sem expor mecanicamente esses metadados no material público.
7. Dimensionar o encontro sem tratá-lo como exposição de 200 minutos e sem impor `Aula → Laboratório`.
8. Usar scaffolding e autonomia conforme definidos no desenho do encontro.
9. Manter no material público apenas informações úteis ao estudante e evitar transcrição de slides, roteiro de condução, lista de atividades ou resumo telegráfico.

Não escolher frameworks, bibliotecas, stack, bibliografia, datas, prazos ou critérios não fornecidos. Não criar slides nesta skill.

## Validar

1. Verificar coerência com a macroprogressão e com os encontros adjacentes existentes.
2. Confirmar que um estudante consegue reconstruir o raciocínio e aprender os conceitos centrais apenas pela página.
3. Confirmar que as seções se encadeiam causalmente, os exemplos sustentam a narrativa e as perguntas recolhíveis preservam investigação antes da análise.
4. Confirmar que IA, quando envolvida, segue a política aprovada.
5. Executar as validações disponíveis, `git diff --check`, `git diff` e `git status`.
6. Relatar arquivos alterados, trajetória, operações cognitivas e validações.

Não fazer commit, push ou publicação sem solicitação explícita.
