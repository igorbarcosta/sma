---
name: revisar-material-didatico
description: Revisa roteiros, práticas, desafios ou projetos de SMA quanto a correção, clareza, coerência pedagógica, operações cognitivas, evidências e prontidão para uso. Use em pedidos de revisão ou diagnóstico; por padrão apenas analise e relate, editando somente quando o usuário pedir explicitamente para aplicar ajustes.
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
- integração entre teoria e prática em ciclos curtos, com prática cedo quando apropriado ao conteúdo e formalização motivada pelo que foi executado ou observado;
- variedade de operações cognitivas e ausência de repetição disfarçada do mesmo padrão de participação e raciocínio em exemplos sucessivos;
- preferência por um sistema ou problema que evolui ao longo do encontro quando isso reduz fragmentação;
- existência de evidência observável da aprendizagem pretendida;
- uso apropriado de worked examples, scaffolding, Peer Instruction, recuperação e interleaving;
- clareza, legibilidade, escopo e dependências;
- coerência da política de IA e responsabilidade do estudante;
- em desafios, prioridade para investigação, diagnóstico, intervenção e evidência;
- no projeto, baseline, comparação, avaliação, redesign e possibilidade legítima de rejeitar múltiplos agentes;
- coerência entre roteiro e prática: comandos, pré-requisitos, saídas, interpretações e alternativas precisam corresponder;
- autonomia real: o estudante consegue começar, executar, observar, interpretar e recuperar-se de falhas previsíveis sem depender do professor.

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
- a página explica a prática, mas não a substitui nem supõe uma explicação oral;
- o estudante encontra o que executar, o que observar, como interpretar e qual é o próximo passo.

### Práticas

- cada comando indicado no roteiro executa como descrito ou falha com mensagem acionável;
- a saída produz evidência para a pergunta proposta, e a análise ajuda a ligar evidência e conceito;
- alternativas controladas são explicitamente identificadas quando servem para isolar um comportamento ou garantir reprodução;
- a prática usa dados seguros e não requer uma configuração oculta, uma ação do professor ou uma inferência não ensinada.

Não propor mudança apenas por preferência editorial nem inventar decisões ausentes.

## Relatar

Classificar achados como:

- **NECESSÁRIO:** erro, contradição, ambiguidade real ou risco relevante;
- **RECOMENDADO:** melhoria clara de aprendizagem ou legibilidade;
- **OPCIONAL:** benefício pequeno;
- **PRESERVAR:** aspecto avaliado que deve permanecer.

Concluir se o material precisa de nova rodada, fica pronto após ajustes pontuais ou está pronto para uso.

Quando houver autorização para editar, modificar somente os pontos aprovados, executar validações pertinentes e inspecionar `git diff` e `git status`. Não fazer commit, push ou publicação sem solicitação explícita.
