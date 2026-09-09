---
name: criar-encontro
description: Cria ou atualiza o roteiro público autoguiado e a prática de um encontro de SMA a partir de um desenho pedagógico já decidido e validado. Use quando o usuário pedir para implementar um encontro específico; não use para decidir a macroprogressão, inventar atividades ou criar os 14 encontros antecipadamente.
---

# Criar encontro

## Preparar

1. Ler `AGENTS.md`.
2. Ler `specs/projeto-pedagogico.md` e `specs/organizacao-dos-materiais.md` integralmente.
3. Ler `specs/avaliacao-e-uso-de-ia.md` quando o encontro se relacionar a uma avaliação, desafio ou projeto.
4. Consultar retrospectivas relevantes da oferta como evidência contextual, nunca como regra.
5. Confirmar que o pedido define suficientemente problema, resultados pretendidos, escopo e operações cognitivas. Diante de decisão pedagógica importante ausente, pedir orientação.

## Implementar

1. Criar ou atualizar `docs/encontros/encontro-XX-<slug>.md` e sua prática em `praticas/encontro-XX/`.
2. Contar uma história conceitual coerente e causal, preservando, sem impor uma fórmula rígida, a trajetória `problema → tensão → investigação → conceito → aplicação → transferência` do desenho aprovado.
3. Construir o roteiro e a prática como uma unidade autoguiada: um estudante deve conseguir começar, executar, observar, interpretar e retomar o percurso sem o professor presente.
4. Explicitar no roteiro o problema, preparação, comandos executáveis a partir da raiz, saídas ou evidências a observar, perguntas de investigação, análise posterior e próximo passo. Antecipar alternativas relevantes e falhas comuns sem transformar a página em roteiro interno.
5. Preferir exemplos recorrentes que carreguem a narrativa; desenvolver exemplos trabalhados, comparações e contraexemplos quando contribuírem para a compreensão.
6. Apresentar perguntas antes da explicação quando a investigação for pedagogicamente útil e oferecer análises ou possíveis respostas recuperáveis que expliquem o raciocínio.
7. Usar operação cognitiva e evidência observável para planejar e validar cada atividade, sem expor mecanicamente esses metadados no material público.
8. Dimensionar o encontro sem tratá-lo como exposição de 200 minutos e sem impor `Aula → Laboratório`.
9. Usar scaffolding e autonomia conforme definidos no desenho do encontro.
10. Quando o conteúdo permitir, iniciar cedo uma experiência concreta e integrar teoria e prática em ciclos curtos de previsão, execução, observação, formalização e aplicação; preferir um sistema ou problema que evolua quando isso reduzir fragmentação.
11. Variar as operações cognitivas ao longo da experiência e verificar se exemplos diferentes não repetem disfarçadamente o mesmo padrão de participação e raciocínio.

Não escolher frameworks, bibliotecas, stack, bibliografia, datas, prazos ou critérios não fornecidos. Não criar slides para encontros novos.

## Validar

1. Verificar coerência com a macroprogressão e com os encontros adjacentes existentes.
2. Confirmar que um estudante consegue reconstruir o raciocínio e aprender os conceitos centrais pelo roteiro e pela prática, sem explicação oral.
3. Confirmar que as seções se encadeiam causalmente, os exemplos sustentam a narrativa e as perguntas recolhíveis preservam investigação antes da análise.
4. Executar os comandos do roteiro e confirmar que saídas, alternativas e evidências descritas permitem ao estudante diagnosticar o que ocorreu; quando houver LLM, confirmar uma alternativa reproduzível ou uma mensagem de erro acionável.
5. Confirmar, quando apropriado ao conteúdo, que a prática começa cedo, gera necessidade para formalizações curtas e permite executar, observar ou modificar algo; verificar também a variedade cognitiva e possíveis repetições disfarçadas.
6. Confirmar que IA, quando envolvida, segue a política aprovada.
7. Executar as validações disponíveis, `git diff --check`, `git diff` e `git status`.
8. Relatar arquivos alterados, trajetória, autonomia de estudo, operações cognitivas e validações.

Não fazer commit, push ou publicação sem solicitação explícita.
