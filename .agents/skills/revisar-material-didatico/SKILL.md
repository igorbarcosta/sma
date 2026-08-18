---
name: revisar-material-didatico
description: Revisa materiais didáticos existentes de SMA quanto a correção, clareza, coerência pedagógica, operações cognitivas, evidências e prontidão para uso. Use em pedidos de revisão ou diagnóstico de encontro, desafio, projeto ou deck; por padrão apenas analise e relate, editando somente quando o usuário pedir explicitamente para aplicar ajustes.
---

# Revisar material didático

## Definir o modo

- Por padrão, analisar e relatar sem alterar arquivos.
- Editar somente mediante pedido explícito para corrigir ou aplicar ajustes.

## Consultar fontes

1. Ler `AGENTS.md`.
2. Ler as specs pertinentes ao material.
3. Consultar materiais adjacentes quando necessário para avaliar dependências e progressão.
4. Consultar retrospectivas relevantes como evidência contextual, sem promovê-las a regra.

## Avaliar

- correção conceitual e independência de framework;
- coerência com o princípio da solução mais simples;
- causalidade entre problema, investigação, formalização, aplicação e transferência;
- adequação entre operação cognitiva declarada e atividade proposta;
- existência de evidência observável da aprendizagem pretendida;
- uso apropriado de worked examples, scaffolding, Peer Instruction, recuperação e interleaving;
- clareza, legibilidade, escopo e dependências;
- coerência da política de IA e responsabilidade do estudante;
- em desafios, prioridade para investigação, diagnóstico, intervenção e evidência;
- no projeto, baseline, comparação, avaliação, redesign e possibilidade legítima de rejeitar múltiplos agentes;
- em slides, narrativa, legibilidade a distância, densidade, contraste, overflow e fidelidade ao roteiro.

Não propor mudança apenas por preferência editorial nem inventar decisões ausentes.

## Relatar

Classificar achados como:

- **NECESSÁRIO:** erro, contradição, ambiguidade real ou risco relevante;
- **RECOMENDADO:** melhoria clara de aprendizagem ou legibilidade;
- **OPCIONAL:** benefício pequeno;
- **PRESERVAR:** aspecto avaliado que deve permanecer.

Concluir se o material precisa de nova rodada, fica pronto após ajustes pontuais ou está pronto para uso.

Quando houver autorização para editar, modificar somente os pontos aprovados, executar validações pertinentes e inspecionar `git diff` e `git status`. Não fazer commit, push ou publicação sem solicitação explícita.
