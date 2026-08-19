# Encontro 01 — O que é um agente?

## Pergunta orientadora

> **O que é um agente?**

Ao final deste encontro, você deverá conseguir analisar um sistema novo, distinguir quais propriedades de agência estão ou não presentes e justificar sua classificação por meio da arquitetura observada — sem depender de critérios superficiais como “usa IA”, “usa uma LLM”, “parece inteligente” ou “conversa com o usuário”.

## Antes da definição: quatro sistemas

Considere os sistemas abaixo sem procurar ainda uma fórmula pronta.

### Sistema A — termostato

Percebe a temperatura e liga ou desliga o aquecimento para manter uma temperatura desejada.

### Sistema B — chamada isolada para uma LLM

Recebe uma pergunta, gera uma resposta e termina.

### Sistema C — workflow determinístico

Recebe um formulário, valida dados, consulta um banco e envia um e-mail seguindo regras previamente definidas.

### Sistema D — sistema orientado por objetivo

Recebe um objetivo, observa informações disponíveis, decide uma ação, executa-a, observa o resultado e pode decidir novamente.

Para cada sistema, registre individualmente:

1. `agente`, `não agente` ou `depende/não tenho certeza`;
2. ao menos uma propriedade que sustentou sua decisão.

Depois, compare suas respostas com as de um colega. Se mudar de opinião, identifique qual argumento provocou a mudança.

**Operação cognitiva:** distinguir e justificar.

**Evidência:** classificação inicial acompanhada de uma propriedade e registro do argumento que eventualmente alterou a classificação.

## Um modelo para investigar agência

Um **agente** é um sistema situado em um **ambiente** que percebe aspectos desse ambiente, toma decisões orientadas por um **objetivo** e age sobre ele com algum grau de **autonomia**.

```text
                ambiente
                   │
               percepção
                   ▼
                 agente
            estado / decisão
                   │
                  ação
                   ▼
                ambiente
```

O comportamento pode formar um ciclo:

```text
perceber → decidir → agir → perceber a consequência → decidir novamente
```

Use estes elementos como dimensões de análise, não como uma checklist rígida:

- **ambiente:** aquilo com que o sistema interage e que pode afetar seu comportamento;
- **percepção:** informação que o sistema obtém do ambiente;
- **ação:** intervenção que o sistema pode produzir no ambiente;
- **objetivo:** condição ou direção que orienta seu comportamento;
- **decisão:** escolha de uma ação diante das informações disponíveis;
- **autonomia:** quanto dessas escolhas pertence ao sistema, dentro dos limites definidos por quem o projetou.

Agência admite graus e casos de fronteira. Sistemas podem receber classificações diferentes quando as propriedades observadas e a argumentação são tecnicamente consistentes.

## Uma LLM é um agente?

Compare as duas arquiteturas:

```text
entrada → LLM → saída
```

```text
objetivo
   ↓
perceber → decidir → agir → observar consequência
              ↑                         │
              └─────────────────────────┘
```

Uma LLM pode fazer parte do mecanismo de decisão de um agente, mas uma LLM não é automaticamente um agente. Da mesma forma, um agente não precisa utilizar IA generativa.

Considere o contraste:

- **Sistema X:** usa uma LLM muito poderosa apenas para gerar uma descrição textual;
- **Sistema Y:** é um termostato antigo que percebe a temperatura e age autonomamente sobre o ambiente.

Qual apresenta mais características de agência? Uma tecnologia mais moderna ou um workflow com muitas etapas não é necessariamente mais agentivo.

**Operação cognitiva:** comparar arquiteturas.

**Evidência:** justificativa que identifica percepção, decisão, ação, objetivo e autonomia, em vez de usar apenas a presença de IA.

## Simulação: pedido 381

Objetivo do sistema:

> **Verifique o pedido 381. Se estiver atrasado, abra uma solicitação de atendimento.**

O ambiente oferece duas ações:

```text
consultar_pedido(id)
abrir_solicitacao(id, motivo)
```

Uma trajetória possível é:

```text
objetivo recebido
→ escolher consultar_pedido(381)
→ perceber status = atrasado
→ interpretar o novo estado
→ escolher abrir_solicitacao(381, "pedido atrasado")
→ perceber solicitação criada
```

Durante a simulação, localize:

- a percepção;
- a decisão;
- a ação;
- o ambiente;
- o objetivo;
- o espaço de autonomia.

Depois, examine o que mudaria se todas as etapas fossem determinadas previamente por condições fixas.

**Operação cognitiva:** explicar uma arquitetura em funcionamento.

**Evidência:** associação de cada evento da trajetória a uma responsabilidade arquitetural e explicação do grau de autonomia observado.

## Caso de fronteira

> Um assistente recebe um pedido do usuário. Uma regra fixa determina qual API será chamada. A LLM apenas transforma o resultado em linguagem natural.

Isso é um agente, um workflow ou depende da definição adotada?

Primeiro, escolha individualmente uma posição e escreva a propriedade decisiva para você. Em seguida, discuta com um colega, vote novamente e compare a qualidade das duas justificativas. O objetivo não é produzir unanimidade, mas tornar explícito onde estão percepção, decisão, ação e autonomia.

**Operação cognitiva:** revisar e defender uma classificação.

**Evidência:** segundo voto acompanhado de justificativa arquitetural, inclusive quando a resposta não mudar.

## Desafio de fronteira em grupo

Cada grupo analisará um sistema: termostato, robô aspirador, chatbot simples, workflow de aprovação, LLM com acesso a uma capacidade externa ou agente de compras orientado por objetivo.

Prepare uma defesa curta neste formato:

> **Nosso sistema apresenta estas propriedades de agência e não apresenta estas outras. Por isso, nossa classificação é...**

Considere:

- O que o sistema percebe e qual é seu ambiente?
- Isso é decisão ou apenas uma condição programada?
- O sistema poderia escolher não agir?
- Aprender é requisito para ser agente?
- Se retirarmos a LLM, ele continua sendo agente?
- Onde começa e termina a autonomia?

As defesas serão breves e poderão ser contestadas pela turma.

**Operação cognitiva:** analisar e justificar.

**Evidência:** defesa que distingue propriedades presentes e ausentes e responde a pelo menos uma contestação com base na arquitetura.

## Síntese

> **Uma LLM não é automaticamente um agente.**

> **Um agente não precisa usar IA generativa.**

> **Mais importante que apenas perguntar “isso é um agente?” é compreender quais responsabilidades, decisões e graus de autonomia existem na arquitetura.**

Retome dois sistemas da abertura e reformule suas classificações usando agora as propriedades arquiteturais estudadas. Sua resposta pode permanecer a mesma; o que deve mudar é a qualidade da justificativa.

**Operação cognitiva:** distinguir e justificar com um modelo mais preciso.

**Evidência:** classificação final comparável à resposta inicial e sustentada por propriedades arquiteturais.

## Trabalho autônomo orientado

Este trabalho é **formativo, sem nota** e faz parte da aprendizagem regular. Pode ser iniciado no laboratório ou realizado em casa, conforme sua preferência e necessidade. Conclua-o ao longo da semana, antes do próximo encontro; o resultado será retomado brevemente no início do Encontro 02.

Escolha um sistema real que você considere agentivo ou possivelmente agentivo. Pode ser ChatGPT, Copilot, Alexa, Waze, um robô aspirador, recomendador, bot, automação residencial, sistema industrial, jogo ou outro sistema relevante.

Responda brevemente:

1. Qual é o ambiente?
2. O que o sistema percebe?
3. O que ele pode fazer?
4. Qual objetivo parece orientar seu comportamento?
5. Que decisões pertencem ao próprio sistema?
6. Onde está a autonomia?
7. Você o considera um agente? Justifique.

Termine com a pergunta:

> **Mesmo que esse sistema possa ser considerado um agente, ele precisava ser um agente?**

**Operação cognitiva:** transferir o modelo de análise para um sistema real e formular uma hipótese para o próximo encontro.

**Evidência:** análise curta que sustenta a classificação por propriedades arquiteturais e questiona a necessidade da agência.

## Próximo encontro

No Encontro 02, retomaremos algumas dessas análises para investigar:

> **Quando vale a pena tornar um sistema agentivo?**
