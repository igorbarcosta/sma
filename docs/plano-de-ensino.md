# Plano de Ensino

## Identificação

**Disciplina:** Sistemas Multiagentes / Agentic AI

**Curso:** Engenharia de Computação

**Linguagem técnica de referência:** Python

## Visão da disciplina

Esta disciplina estuda Sistemas Multiagentes com foco contemporâneo em sistemas agentivos baseados em modelos de linguagem de grande porte (LLMs). Conceitos clássicos de Sistemas Multiagentes aparecem quando oferecem modelos duráveis para compreender os sistemas atuais, e não como um bloco histórico separado.

O semestre será orientado por uma pergunta de engenharia: **qual é a solução mais simples adequada ao problema?** A progressão arquitetural de referência é:

```text
software determinístico
→ uso simples de LLM
→ workflow
→ agente
→ sistema multiagente
```

Cada aumento de complexidade precisa responder a uma necessidade e ser sustentado por evidências. Frameworks, bibliotecas e providers são meios substituíveis; compreender, projetar, diagnosticar e avaliar sistemas agentivos é o objetivo central.

## Resultados de aprendizagem

Ao final da disciplina, você deverá ser capaz de:

1. analisar e distinguir diferentes graus de agência;
2. projetar agentes baseados em LLM;
3. projetar contexto, estado e memória;
4. integrar ferramentas e ambiente;
5. diagnosticar e avaliar agentes;
6. justificar ou rejeitar o uso de múltiplos agentes;
7. projetar interação, comunicação e coordenação multiagente;
8. implementar arquiteturas agentivas contemporâneas sem dependência conceitual de um framework específico;
9. avaliar criticamente e defender decisões arquiteturais com base em evidências.

## Como a aprendizagem será organizada

A disciplina será uma sequência de **14 experiências semanais**, não uma divisão fixa entre aula e laboratório. Cada quarta-feira possui quatro tempos de 50 minutos. Conforme a necessidade do encontro, esse período poderá combinar momentos conduzidos pelo professor, investigação e discussão, prática assistida, estúdio de engenharia e trabalho autônomo orientado.

A composição muda de acordo com o problema em estudo e com a autonomia desenvolvida pela turma. Por isso, os quatro tempos não seguem uma distribuição rígida: explicação, investigação, discussão, prática e trabalho autônomo são recursos articulados em uma mesma trajetória de aprendizagem.

O trabalho autônomo orientado é formativo e sem nota por padrão, possui uma operação cognitiva explícita e não se confunde com Desafio, Avaliação ou Projeto. Pode ser realizado no laboratório ou em casa, sem diferença pedagógica entre os locais, normalmente ao longo da semana e antes do encontro seguinte, que procurará retomar brevemente o resultado produzido. Quando uma atividade compuser a nota, será identificada explicitamente como instrumento avaliativo. Essa organização pedagógica não define nem altera regras institucionais de frequência, que permanecem uma questão administrativa separada.

O site reúne conteúdos e orientações permanentes. Datas, entregas, comunicação e notas serão tratadas no Google Classroom; a visão atual do semestre ficará no [Cronograma](cronograma.md).

## Metodologia

Os encontros partirão, predominantemente, de problemas e necessidades antes de formalizar conceitos. A trajetória mais comum será:

```text
problema
→ previsão ou investigação
→ formalização
→ aplicação
→ transferência
```

Você será convidado a formular previsões, investigar comportamentos, comparar alternativas e explicar evidências antes ou depois da apresentação de modelos conceituais. Essa aprendizagem ativa será guiada: quando a novidade ou a carga cognitiva for alta, exemplos resolvidos tornarão visível o raciocínio esperado; no início haverá mais apoio, e esse *scaffolding* será retirado progressivamente à medida que a autonomia aumentar.

Quando houver interpretações concorrentes plausíveis, discussões no formato de Peer Instruction poderão ajudar a explicitar e revisar modelos mentais. Conceitos importantes reaparecerão por recuperação espaçada, e estratégias poderão ser intercaladas quando a comparação ajudar a distinguir quando e por que usar cada uma.

Cada atividade tem uma operação cognitiva pretendida, como prever, distinguir, comparar, explicar, diagnosticar, aplicar, transferir, projetar, avaliar evidências ou justificar uma decisão. Produzir um artefato não basta, por si só, para demonstrar compreensão: o trabalho deve gerar evidências observáveis do raciocínio. Por isso, o feedback buscará as ideias e os modelos mentais que produziram uma decisão ou um erro.

Nas atividades experimentais, o ciclo esperado é formular uma hipótese, realizar uma intervenção, observar o comportamento e analisar evidências. O objetivo não é apenas fazer o sistema funcionar, mas compreender por que ele se comporta de determinada maneira e em que condições uma alternativa é melhor.

## Conteúdo e progressão do semestre

A progressão parte da compreensão da agência, passa pela construção e avaliação de agentes e chega à decisão fundamentada sobre arquiteturas multiagente. As perguntas abaixo definem a direção conceitual de cada encontro; elas não representam uma sequência de exposições nem uma ementa rígida.

| Encontro | Pergunta orientadora | Foco principal |
| ---: | --- | --- |
| 1 | **O que é um agente?** | Compreender e distinguir graus de agência. |
| 2 | **Quando vale a pena tornar um sistema agentivo?** | Comparar soluções determinísticas, uso simples de LLM, workflows e agentes. |
| 3 | **Do que é feito um agente baseado em LLM?** | Construir um modelo dos componentes e responsabilidades de um agente. |
| 4 | **Como um agente passa de responder para agir?** | Integrar ferramentas e ambiente para produzir ações. |
| 5 | **Como contexto, estado e memória afetam o comportamento?** | Projetar e avaliar a informação disponível ao agente. |
| 6 | **Como observar e diagnosticar um agente?** | Investigar comportamento, falhas e evidências. |
| 7 | **O que um segundo agente resolve que o primeiro não resolve?** | Formular e testar justificativas para múltiplos agentes. |
| 8 | **Como dois agentes trabalham juntos?** | Projetar interação, comunicação e coordenação. |
| 9 | **Como organizar vários agentes?** | Comparar formas de organização multiagente. |
| 10 | **Como agentes e capacidades independentes se conectam?** | Compreender interoperabilidade entre agentes e capacidades. |
| 11 | **O que pode dar errado quando damos autonomia a agentes?** | Analisar riscos, limites e mecanismos de controle. |
| 12 | **Como avaliar se uma arquitetura agentiva realmente é melhor?** | Comparar arquiteturas com critérios e evidências. |
| 13 | **Como melhorar um sistema a partir de suas falhas?** | Diagnosticar, redesenhar e reavaliar o sistema. |
| 14 | **Que sistema deveríamos realmente construir?** | Sintetizar evidências e defender decisões arquiteturais. |

Em conjunto, os encontros percorrem a seguinte narrativa:

```text
compreender agência
→ construir
→ agir
→ gerenciar informação
→ observar
→ justificar múltiplos agentes
→ interagir
→ organizar
→ interoperar
→ controlar
→ comparar
→ redesenhar
→ defender
```

## Avaliação

Os instrumentos avaliam funções complementares da aprendizagem: domínio individual, investigação prática e integração longitudinal. A nota da disciplina será composta assim:

| Instrumento | Composição | Peso |
| --- | --- | ---: |
| **Avaliações individuais** | Três avaliações de 10% cada | **30%** |
| **Desafios práticos** | Quatro desafios; contam as três melhores notas | **20%** |
| **Projeto integrador** | Desenvolvimento e avaliação longitudinal | **50%** |

### Avaliações individuais — 30%

Haverá três avaliações individuais, presenciais, em papel e sem uso de IA, cada uma valendo 10% da nota. Elas priorizarão compreensão, diagnóstico, decisão arquitetural, transferência e justificativa, em vez de reprodução mecânica de conteúdo.

Ao final do percurso regular, haverá uma **avaliação substitutiva cumulativa**. Ela poderá substituir uma avaliação perdida ou melhorar a menor nota entre as três avaliações, neste segundo caso somente quando o resultado da substitutiva for superior. A substitutiva troca apenas uma avaliação.

### Desafios práticos — 20%

Haverá quatro desafios individuais, dos quais serão consideradas as três melhores notas. O conjunto vale 20% da nota da disciplina, e o uso de IA é permitido.

Sempre que for pedagogicamente adequado, os desafios partirão de artefatos ou sistemas parcialmente prontos, evitando que a atividade principal seja apenas construir algo do zero. Um fluxo típico será:

```text
previsão ou diagnóstico inicial
→ investigação
→ intervenção
→ execução
→ evidência
→ conclusão
```

Os desafios privilegiarão a capacidade de compreender o estado inicial, levantar hipóteses, intervir de forma intencional e sustentar conclusões com o comportamento observado.

### Projeto integrador — 50%

O projeto integrador é longitudinal, pode ser realizado individualmente ou em dupla e começa depois que a turma tiver desenvolvido modelos mentais básicos de engenharia de agentes. Em dupla, a nota do projeto será a mesma para os dois integrantes.

O percurso esperado é:

```text
problema
→ critérios de sucesso
→ baseline
→ solução com um agente
→ avaliação
→ hipótese multiagente
→ versão multiagente experimental
→ comparação
→ redesign
→ conclusão
```

A solução final **não precisa ser multiagente**. O projeto exige investigar experimentalmente essa alternativa, compará-la ao baseline e à solução com um agente e decidir com base em evidências. Concluir de forma bem fundamentada que a arquitetura multiagente não compensou sua complexidade é um resultado válido e desejável.

Os milestones intermediários servirão principalmente para feedback e correção de trajetória, não como uma coleção de pequenas notas. Os 50% do projeto serão distribuídos pela seguinte rubrica:

| Critério | Peso na nota da disciplina |
| --- | ---: |
| Problema, critérios e baseline | **7%** |
| Arquitetura e implementação | **15%** |
| Avaliação e evidências | **15%** |
| Diagnóstico, redesign e análise crítica | **10%** |
| Reprodutibilidade e comunicação técnica | **3%** |
| **Total do projeto** | **50%** |

## Uso de inteligência artificial

A disciplina possui dois regimes simples de uso de IA:

| Atividade | Regime |
| --- | --- |
| **Avaliações individuais** | Sem IA |
| **Desafios práticos e projeto integrador** | IA permitida |

Usar ou não usar IA não gera bônus nem penalidade por si só. Código, texto ou arquitetura produzidos com IA serão avaliados pelos mesmos critérios que qualquer outro artefato. Você continua responsável por compreender, verificar, justificar e ser capaz de modificar tudo que entrega.

Uma resposta de IA é uma proposta a ser examinada, não uma fonte de verdade. “A IA disse” não constitui evidência técnica. Quando a IA for permitida, o ciclo de trabalho esperado é:

```text
delegar
→ inspecionar
→ testar
→ criticar
→ modificar
→ avaliar
```

Permitir IA não reduz a exigência de domínio, reprodutibilidade ou evidência. Também não será exigido um diário de prompts.

## Ambiente técnico

As atividades usarão Python 3.12 e `uv` para manter projeto, ambiente virtual e dependências de forma reproduzível. Você poderá trabalhar em um clone local ou no GitHub Codespaces; o Codespaces é uma alternativa, não um requisito.

Gemini é o provider didático inicial. Outros providers poderão aparecer quando forem pedagogicamente relevantes, sem mudar os conceitos centrais da disciplina. As instruções de preparação, credenciais e diagnóstico estão em [Ambiente de desenvolvimento](materiais/ambiente.md).

## Referências e materiais

Os materiais permanentes da disciplina serão publicados neste site. A bibliografia detalhada será consolidada posteriormente na página de [Referências](materiais/referencias.md), quando estiver definida.
