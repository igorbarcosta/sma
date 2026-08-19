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

### Páginas públicas

**Autonomia de estudo**

- o estudante consegue aprender ou revisar sem a presença do professor;
- os conceitos estão realmente explicados, e não apenas nomeados;
- exemplos e respostas possuem análise suficiente para tornar o raciocínio reconstruível.

**Storytelling**

- existe uma pergunta ou tensão que move a narrativa;
- as seções se encadeiam causalmente e o conceito aparece porque surgiu uma necessidade;
- não há rupturas entre blocos nem sensação de coleção de tópicos;
- exemplos carregam a narrativa, em vez de funcionar apenas como ilustrações soltas.

**Separação de funções**

- a página funciona como material de estudo, não como roteiro interno;
- metadados pedagógicos internos não estão expostos sem necessidade;
- a página não é uma duplicação dos slides.

### Slides

- o arco narrativo aprovado permanece visível e cada frame ajuda a movê-lo;
- casos, perguntas, revelações, contrastes e progressão visual sustentam o storytelling;
- todas as ideias, exemplos, contraexemplos, comparações, perguntas, análises, exemplos trabalhados, sínteses e transições conceitualmente importantes da página estão representados;
- perguntas relevantes recebem posteriormente resposta ou análise no próprio deck, sem revelação prematura e sem depender das notas;
- o deck pode ser compreendido posteriormente pelo estudante em HTML ou PDF;
- o minimalismo resulta de baixa densidade por frame, não de omissões para reduzir a quantidade de slides;
- o deck preserva ritmo e legibilidade sem copiar mecanicamente as explicações detalhadas da página pública;
- detectar explicitamente o caso de um deck visualmente bonito, mas conceitualmente incompleto.

Não propor mudança apenas por preferência editorial nem inventar decisões ausentes.

## Relatar

Classificar achados como:

- **NECESSÁRIO:** erro, contradição, ambiguidade real ou risco relevante;
- **RECOMENDADO:** melhoria clara de aprendizagem ou legibilidade;
- **OPCIONAL:** benefício pequeno;
- **PRESERVAR:** aspecto avaliado que deve permanecer.

Concluir se o material precisa de nova rodada, fica pronto após ajustes pontuais ou está pronto para uso.

Quando houver autorização para editar, modificar somente os pontos aprovados, executar validações pertinentes e inspecionar `git diff` e `git status`. Não fazer commit, push ou publicação sem solicitação explícita.
