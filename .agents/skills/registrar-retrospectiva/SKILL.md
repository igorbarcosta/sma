---
name: registrar-retrospectiva
description: Registra ou organiza a retrospectiva de um encontro real da oferta de SMA a partir de evidências fornecidas pelo professor. Use após um encontro realizado para criar o arquivo correspondente em `retrospectivas/`; não use para antecipar retrospectivas, inventar observações ou alterar specs automaticamente.
---

# Registrar retrospectiva

## Preparar

1. Ler `AGENTS.md` e `specs/retrospectivas.md`.
2. Confirmar oferta e número do encontro.
3. Usar somente evidências fornecidas ou observadas no contexto autorizado.
4. Separar fatos de interpretações; diante de lacunas, registrá-las como incerteza em vez de preenchê-las.

## Registrar

Criar ou atualizar `retrospectivas/<oferta>/encontro-XX.md` com:

1. Observado;
2. Interpretação provisória;
3. Preservar;
4. Ajustes locais;
5. Propagar nesta oferta;
6. Próxima oferta;
7. Operação cognitiva planejada, evidência observada e avaliação cautelosa de sua ocorrência.

Não transformar observação isolada em regra. Não reescrever retroativamente o que ocorreu. Não atualizar specs durante esta skill, salvo pedido explícito e decisão durável já tomada pelo professor.

## Validar

1. Confirmar que toda afirmação factual possui base nas evidências disponíveis.
2. Confirmar que hipóteses estão marcadas como provisórias.
3. Confirmar que sugestões para próxima oferta continuam candidatas.
4. Executar `git diff --check`, inspecionar `git diff` e `git status`.
5. Relatar o arquivo alterado e incertezas preservadas.

Não fazer commit, push ou publicação sem solicitação explícita.
