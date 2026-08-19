# Encontro 01 — O que é um agente?

**Slides:** [Apresentação HTML](../slides/rendered/encontro-01-o-que-e-um-agente.html) · [PDF](../slides/rendered/encontro-01-o-que-e-um-agente.pdf)

**Pergunta orientadora**

> **O que é um agente?**

Ao final deste encontro, você deverá conseguir analisar um sistema novo, distinguir quais propriedades de agência estão ou não presentes e justificar sua classificação pela arquitetura observada. Para chegar lá, não começaremos por uma definição. Começaremos por um incômodo: sistemas muito diferentes recebem o mesmo rótulo, enquanto sistemas parecidos são classificados de maneiras opostas.

## Achamos que sabemos o que é um agente

Considere quatro sistemas:

- um **termostato** percebe a temperatura e liga ou desliga o aquecimento para manter uma condição desejada;
- uma **LLM isolada** recebe uma pergunta, produz uma resposta e termina;
- um **workflow** recebe um formulário, valida dados, consulta um banco e envia um e-mail seguindo regras predefinidas;
- um **sistema orientado por objetivo** observa informações disponíveis, escolhe uma ação, executa-a, observa o resultado e pode escolher novamente.

Antes de continuar, classifique cada um como `agente`, `não agente` ou `depende`. Registre também a propriedade que mais pesou em sua decisão.

> O que exatamente estamos usando para chamar alguma coisa de agente?

??? "Ver possível análise"

    É comum usar como critério aquilo que mais chama atenção: linguagem sofisticada, inteligência aparente, novidade tecnológica ou presença de IA generativa. Esses critérios não se sustentam bem quando confrontamos os quatro sistemas.

    Se linguagem fosse requisito, o termostato nunca poderia apresentar agência. Se IA generativa bastasse, toda chamada isolada a uma LLM seria um agente, mesmo quando outro programa controla integralmente quando chamá-la e o que fazer com a resposta. Se modernidade fosse decisiva, estaríamos classificando a tecnologia, não as responsabilidades do sistema.

    Ainda não precisamos concordar sobre todos os casos. Precisamos de um modelo que explique nossas decisões melhor do que “parece inteligente”.

## O termostato cria o primeiro problema

O termostato não conversa, não usa uma LLM, não aprende e provavelmente não parece inteligente no sentido contemporâneo. Mesmo assim, ele mantém uma relação contínua com algo fora dele.

Imagine que a temperatura desejada seja 22 °C. O termostato lê 19 °C, compara essa informação com a condição desejada e liga o aquecimento. Mais tarde, lê 22 °C e o desliga. Há limites estreitos e regras simples, mas também há uma estrutura reconhecível:

```text
temperatura observada
→ comparação com a condição desejada
→ escolha entre ligar e desligar
→ mudança no ambiente
→ nova temperatura observada
```

O termostato observa uma propriedade do ambiente, possui uma condição que orienta seu comportamento, decide entre possibilidades previstas e age sobre esse ambiente. Sua autonomia é pequena, mas não é necessário confundi-la com inteligência generativa.

> Se o termostato possui várias propriedades de agência, a inteligência generativa pode ser nosso critério principal?

??? "Ver possível análise"

    Não. O termostato funciona como contraexemplo: ele mostra que podemos encontrar percepção, decisão orientada por uma condição, ação e retorno do ambiente sem linguagem ou IA generativa.

    Isso ainda não encerra a classificação do termostato. Dependendo da definição e do grau de autonomia exigido, alguém pode tratá-lo como um agente muito simples ou apenas como um controlador. O ponto decisivo é outro: “usa IA moderna” não serve como fronteira geral para agência.

## A LLM cria o problema oposto

Agora considere uma LLM em uma chamada isolada:

```text
entrada → modelo → saída
```

Ela pode explicar um assunto difícil, comparar alternativas e produzir linguagem sofisticada. Porém, nessa arquitetura, outro componente normalmente determina quando o modelo é chamado, fornece a entrada, recebe a saída e decide se algo acontecerá depois.

Pergunte quem controla quando a chamada começa, se a resposta produzirá algum efeito, se outra informação será consultada, se haverá uma nova chamada e quando o processo termina.

Uma resposta complexa não transfere automaticamente essas responsabilidades para o modelo. A LLM transforma a entrada em uma saída; o restante da arquitetura pode continuar inteiramente sob controle externo.

??? "Por que isso é uma tensão importante?"

    Porque o sistema tecnologicamente mais sofisticado pode possuir menos responsabilidades agentivas naquela arquitetura do que um dispositivo simples. A aparência de inteligência e a distribuição de responsabilidades não são a mesma coisa.

    Uma LLM pode integrar o mecanismo de decisão de um agente. Mas sua presença, isoladamente, não nos diz quem percebe o ambiente, escolhe o próximo passo, produz efeitos ou observa consequências.

Chegamos ao mesmo problema por duas direções: o termostato apresenta propriedades de agência sem IA generativa; a LLM isolada apresenta inteligência linguística sem necessariamente controlar uma interação. Precisamos olhar para a arquitetura.

## Precisamos de um modelo melhor

Um **agente** pode ser compreendido como um sistema situado em um **ambiente**, capaz de perceber aspectos desse ambiente, tomar decisões orientadas por um **objetivo** e agir com algum grau de **autonomia**.

```text
                     ambiente
              percepção │ ▲ consequência
                        ▼ │
                    ┌─────────┐
        objetivo ──▶│ agente  │
                    │ decisão │
                    └─────────┘
                        │
                       ação
                        ▼
                     ambiente
```

Esses conceitos formam um modelo de análise, não uma checklist automática.

O **ambiente** é aquilo com que o sistema interage e que pode afetar seu comportamento. Para o termostato, inclui a temperatura do espaço e o equipamento de aquecimento. Para um sistema de atendimento, pode incluir o cadastro de pedidos e o serviço que registra solicitações.

A **percepção** é a informação que chega do ambiente e fica disponível para orientar o comportamento. Ler `19 °C` é uma percepção. Receber `status = atrasado` de um serviço também é. Perceber não significa necessariamente usar sensores físicos: consultar um banco ou receber uma resposta de API pode cumprir esse papel.

O **objetivo** fornece uma direção. “Manter 22 °C” e “verificar o pedido e agir se estiver atrasado” são condições que permitem avaliar quais ações fazem sentido. Um objetivo não precisa ser formulado em linguagem natural nem inventado pelo próprio sistema.

A **decisão** é a seleção do que fazer diante das informações disponíveis. Ela pode ser produzida por regras, modelos estatísticos, uma LLM ou outros mecanismos. Para analisar agência, importa localizar que escolha existe e a quem pertence a responsabilidade por ela.

A **ação** é uma intervenção ou consulta que atravessa a fronteira entre sistema e ambiente. Ligar o aquecimento altera o ambiente; consultar um pedido obtém informação dele; abrir uma solicitação registra uma nova condição nele.

A **autonomia** descreve quanto da seleção e continuidade das ações pertence ao sistema dentro dos limites definidos por quem o projetou. Autonomia não significa liberdade ilimitada. Todo sistema opera com capacidades, regras e fronteiras. A pergunta útil é: dentro desses limites, quem determina o próximo passo?

Volte aos dois exemplos. No termostato, o ambiente é o espaço controlado; a temperatura é percebida; a condição desejada orienta a decisão; ligar ou desligar são ações; e o dispositivo executa esse ciclo sem uma ordem humana a cada leitura. Na chamada isolada à LLM, há entrada e saída, mas a arquitetura mostrada ainda não atribui ao modelo a responsabilidade por continuar a interação ou agir sobre outro ambiente.

## Agência como ciclo

Uma transformação isolada pode ser valiosa:

```text
entrada → transformação → saída
```

Mas uma interação orientada por objetivo pode continuar depois da primeira saída:

```text
perceber
→ decidir
→ agir
→ perceber a consequência
→ decidir novamente
```

O retorno do ambiente importa porque uma ação pode falhar, revelar informação nova ou mudar a situação. O sistema não deveria presumir que o mundo permaneceu como estava antes da ação.

No termostato, ligar o aquecimento não encerra o problema: a temperatura precisa ser observada novamente. Sem essa nova percepção, o aquecimento poderia continuar ligado mesmo depois de atingir a condição desejada. O ciclo liga cada decisão às consequências da anterior.

Isso não significa que todo agente precise repetir indefinidamente ou realizar muitas etapas. Significa que, quando há continuidade, o que acontece depois pode depender do que o ambiente devolveu.

## Exemplo trabalhado — pedido 381

Um sistema recebe o seguinte objetivo:

> **Verifique o pedido 381. Se estiver atrasado, abra uma solicitação de atendimento.**

O ambiente oferece duas ações:

```text
consultar_pedido(id)
abrir_solicitacao(id, motivo)
```

Vamos acompanhar a trajetória inteira.

### 1. O objetivo chega

O sistema sabe qual pedido investigar e qual condição justificaria uma solicitação. Ainda não sabe se o pedido está atrasado. Abrir a solicitação imediatamente seria agir sem a informação necessária.

### 2. O sistema decide consultar

Entre as ações disponíveis, escolhe:

```text
consultar_pedido(381)
```

Essa é uma ação porque consulta algo no ambiente. A decisão foi consultar antes de abrir uma solicitação. Até aqui, o sistema transformou uma lacuna — “não sei o status” — em uma busca por percepção relevante.

### 3. O ambiente responde

```text
status = atrasado
```

Agora existe uma nova percepção. Antes da consulta, o sistema conhecia o objetivo, mas não a situação do pedido. Depois dela, possui a informação que permite distinguir entre agir e encerrar sem abrir uma solicitação.

### 4. A nova informação sustenta outra decisão

Como o status satisfaz a condição indicada no objetivo, o sistema escolhe:

```text
abrir_solicitacao(381, "pedido atrasado")
```

Essa ação altera o ambiente: antes não havia a solicitação; depois, espera-se que haja. A segunda escolha só faz sentido por causa da percepção obtida na etapa anterior.

### 5. O ambiente confirma a consequência

```text
solicitação criada
```

A confirmação é uma nova percepção. Ela permite ao sistema saber que a ação produziu o efeito esperado. Se o ambiente respondesse `serviço indisponível`, a situação seria diferente; a próxima decisão teria de considerar essa consequência.

A trajetória completa pode ser mapeada assim:

```text
objetivo
→ percepção inicial: ainda não conheço o status
→ decisão: preciso consultar
→ ação: consultar_pedido(381)
→ nova percepção: status = atrasado
→ nova decisão: devo abrir a solicitação
→ ação: abrir_solicitacao(...)
→ nova percepção: solicitação criada
```

O exemplo mostra mais do que uma sequência de funções. Ele permite localizar o que o sistema sabia, o que precisava descobrir, por que escolheu cada ação e como o ambiente mudou o passo seguinte.

## E se tudo estivesse escrito em `if/else`?

Suponha que a trajetória do pedido tenha sido programada com condições fixas. Isso elimina automaticamente a agência?

??? "Ver possível análise"

    Não. Software determinístico também pode perceber, decidir segundo regras e agir sobre um ambiente. Um termostato clássico é um bom exemplo. `if/else` descreve um possível mecanismo de decisão; não resolve sozinho a classificação arquitetural.

    Ao mesmo tempo, não devemos chamar qualquer sequência condicional de agente. Precisamos observar onde as escolhas estão predeterminadas, qual espaço de decisão existe e quem determina o próximo passo. Se um workflow fixa toda a ordem e cada condição apenas seleciona um ramo já especificado, sua autonomia pode ser muito limitada. Se um sistema recebe um objetivo e seleciona entre ações conforme novas percepções, há uma responsabilidade diferente, mesmo que partes dessa seleção usem regras.

Autonomia admite graus. O objetivo da análise não é substituir “usa LLM” por “tem `if/else`” como novo atalho, mas explicar a distribuição de responsabilidades. Essa questão abrirá um problema ainda mais importante: mesmo quando podemos construir um sistema agentivo, isso é necessário?

## LLM, workflow e agente

Esses termos descrevem coisas diferentes e não formam uma taxonomia absoluta.

| Arquitetura | Exemplo concreto | Responsabilidade decisiva |
|---|---|---|
| LLM em chamada isolada | recebe um texto, redige um resumo e devolve a saída | outro componente controla quando chamar e o que fazer depois |
| Workflow | valida um formulário, consulta um cadastro e envia um e-mail em ordem definida | o fluxo determina previamente o próximo passo ou ramo |
| Agente | recebe um objetivo, observa a situação e escolhe entre ações permitidas | o sistema possui algum espaço de decisão orientado pelo objetivo |

A presença de uma LLM não determina sozinha a arquitetura. Um workflow pode chamar uma LLM e várias APIs sem delegar ao sistema a escolha do próximo passo. Um agente pode usar regras simples e ainda possuir alguma autonomia dentro de seu ambiente.

Considere o pedido 381. Se o programa sempre executar `consultar` e depois uma condição fixa decidir `abrir` ou `encerrar`, podemos descrevê-lo como workflow. Se o sistema receber o objetivo, dispuser de várias ações e decidir quais usar conforme as respostas do ambiente, cresce a responsabilidade agentiva. O comportamento externo pode até parecer semelhante; a diferença está em quem controla a trajetória.

## O que não é requisito para ser agente?

### Precisa usar IA generativa?

Não. O termostato mostra percepção, ação e orientação por uma condição sem IA generativa. Uma LLM é um mecanismo possível dentro de uma arquitetura, não um requisito de agência.

### Precisa conversar?

Não. Conversa é uma forma de interação. Robôs, controladores e sistemas de software podem perceber e agir sem interface conversacional. Um chatbot, por outro lado, pode conversar sem controlar nenhuma ação além de produzir texto.

### Precisa aprender?

Não. Um sistema pode manter seu comportamento por regras fixas e ainda interagir autonomamente com o ambiente. Aprendizagem pode alterar como ele decide ao longo do tempo, mas não é condição necessária para reconhecer propriedades de agência.

### Precisa ter memória complexa?

Não. Para que uma percepção influencie a decisão corrente, algum dado precisa estar disponível naquele momento. Isso não exige uma arquitetura sofisticada de memória. O aprofundamento desse tema pertence a outra etapa da disciplina.

### Precisa ser sofisticado?

Não. Sofisticação tecnológica e agência são dimensões diferentes. Um sistema simples pode assumir responsabilidades agentivas estreitas; um sistema sofisticado pode executar apenas uma transformação comandada externamente.

### Precisa ser imprevisível?

Não. Imprevisibilidade não prova autonomia nem qualidade. Um sistema determinístico pode agir conforme percepções; um sistema aleatório pode produzir saídas imprevisíveis sem perseguir objetivo algum. O que interessa é como objetivo, percepção, decisão e ação se relacionam.

## Casos de fronteira

Casos de fronteira são úteis porque obrigam a justificar a classificação. Em vez de procurar apenas o rótulo correto, localize a responsabilidade decisiva.

### Chatbot simples

Ele recebe uma mensagem e devolve uma resposta. Isso basta para chamá-lo de agente?

??? "Ver possível análise"

    Depende da arquitetura e da definição adotada. Se ele apenas executa `mensagem → resposta`, o caso se aproxima da chamada isolada à LLM: há interação linguística, mas pouco espaço para escolher ações ou conduzir um ciclo orientado por objetivo. Se puder decidir entre responder, pedir informação e agir sobre sistemas externos, a análise muda.

### Robô aspirador

Ele percebe obstáculos, muda de direção e continua limpando. Onde está sua autonomia?

??? "Ver possível análise"

    O ambiente é o espaço físico; sensores fornecem percepções; movimentar-se e aspirar são ações; limpar orienta o comportamento. Mesmo com regras determinísticas, o próximo movimento pode depender do que foi percebido. A autonomia é limitada pelas capacidades e regras do robô, mas existe uma interação contínua com consequências observáveis.

### Workflow de aprovação

O sistema encaminha uma solicitação ao gestor, espera a resposta e, se aprovada, envia ao financeiro. Há percepção e ação. Isso o torna agente?

??? "Ver possível análise"

    Não há resposta única sem conhecer a arquitetura. Em um workflow convencional, o fluxo completo e seus ramos já determinam quem recebe cada etapa; o sistema executa a trajetória especificada. Podemos reconhecer percepção e ação sem atribuir grande autonomia. A justificativa deve dizer quem escolhe o próximo passo, não apenas contar quantas integrações existem.

### LLM com capacidade externa

Uma LLM pode consultar um cadastro e enviar mensagens. A presença dessas capacidades basta?

??? "Ver possível análise"

    Não. Precisamos saber quem seleciona a capacidade e em que condições. Se outro programa sempre manda consultar e depois enviar, a LLM pode estar apenas preenchendo argumentos ou redigindo texto dentro de um workflow. Se o sistema escolhe entre capacidades conforme objetivo e percepções, ele assume mais responsabilidade pela trajetória.

### Assistente com API escolhida por regra fixa

Uma regra fixa determina qual API será chamada; a LLM apenas transforma o resultado em linguagem natural. Agente, workflow ou depende?

??? "Ver possível análise"

    É razoável classificá-lo como workflow com um componente de LLM, pois a regra externa escolhe a ação e a LLM não controla o próximo passo. Também é possível defender um grau mínimo de agência para o sistema completo se a definição usada valorizar a interação autônoma do conjunto. Em qualquer caso, a justificativa deve explicitar que a escolha da API pertence à regra, não à LLM.

Respostas diferentes podem ser tecnicamente defensáveis. O que não basta é justificar com “tem IA”, “fala com o usuário” ou “usa uma API”.

## Verifique sua compreensão

### 1. Irrigação da estufa

Um sistema lê a umidade do solo a cada dez minutos. Se estiver abaixo de um limite, abre a válvula por dois minutos e depois volta a medir. Identifique ambiente, percepção, objetivo, decisão e ação. Onde está a responsabilidade decisiva?

??? "Ver possível resposta"

    O ambiente inclui solo, água e válvula; a leitura de umidade é percepção; manter a umidade acima do limite orienta o comportamento; abrir ou não a válvula é a decisão; abrir a válvula é a ação. A responsabilidade decisiva está no próprio sistema executar novamente a medição e selecionar a ação prevista sem uma ordem externa a cada ciclo. Sua autonomia é estreita e determinística, mas isso não elimina as propriedades observadas.

### 2. Gerador de parecer

Ao clicar em um botão, um programa envia um documento a uma LLM, recebe um parecer e o exibe. O programa não consulta outras fontes nem executa outra ação. O que impede concluir apenas pela presença da LLM que se trata de um agente?

??? "Ver possível resposta"

    O clique inicia uma transformação isolada, e a arquitetura descrita não atribui ao modelo a escolha de quando agir, o que consultar depois ou como produzir efeitos no ambiente. A linguagem pode ser sofisticada, mas a continuidade e as ações permanecem determinadas externamente.

### 3. Monitor de estoque

Um sistema recebe o objetivo “reduzir faltas de produtos”. Ele pode consultar estoque, vendas e prazo de fornecedores, mas uma regra externa obriga sempre a mesma ordem de consultas e calcula automaticamente a quantidade comprada. O sistema apenas redige a justificativa final. Qual componente possui a responsabilidade decisiva?

??? "Ver possível resposta"

    A regra externa controla a trajetória e calcula a ação. O componente que redige a justificativa não passa a decidir só porque usa linguagem. O sistema completo pode perceber e agir, mas o espaço de decisão descrito é pequeno; por isso, workflow é uma classificação bem sustentada.

### 4. Dois sistemas, mesma saída

Dois programas abrem uma solicitação para o pedido 381. No primeiro, uma sequência fixa controla consulta e abertura. No segundo, o sistema recebe o objetivo e escolhe entre consultar, abrir, pedir esclarecimento ou encerrar conforme cada resposta. Por que a mesma saída final não prova que as arquiteturas possuem o mesmo grau de agência?

??? "Ver possível resposta"

    Porque agência diz respeito também à distribuição das responsabilidades durante a trajetória. O primeiro programa recebe o caminho; o segundo seleciona o próximo passo dentro de um conjunto de possibilidades orientado por objetivo. Observar apenas a solicitação criada apaga as decisões que produziram o resultado.

## Síntese

Nosso caminho começou com uma intuição plausível: talvez inteligência, conversa ou IA generativa definissem agência. O termostato desafiou essa ideia ao apresentar percepção, decisão, ação e retorno do ambiente sem nenhuma dessas características. A LLM isolada mostrou o problema oposto: linguagem sofisticada sem responsabilidade automática pela continuidade da interação.

Por isso, deslocamos a análise da aparência para a arquitetura:

```text
inteligência parecia definir agência
→ o termostato contrariou essa intuição
→ a LLM isolada revelou o contraste oposto
→ precisamos localizar responsabilidades na arquitetura
→ ambiente, percepção, objetivo, decisão, ação e autonomia
→ agência passa a ser distinguida e justificada por essas relações
```

Leve três ideias centrais:

- uma LLM não é automaticamente um agente;
- um agente não precisa usar IA generativa;
- mais importante que aplicar um rótulo é explicar quem percebe, quem decide, o que pode ser feito, qual objetivo orienta o comportamento e onde existe autonomia.

Volte agora às quatro classificações do início. Elas podem permanecer iguais. O que deve mudar é a qualidade da justificativa.

## Trabalho autônomo orientado

Este trabalho é **formativo e sem nota**. Você pode iniciá-lo no laboratório ou realizá-lo em casa, conforme sua preferência e necessidade. Desenvolva-o durante a semana; o resultado será retomado brevemente no próximo encontro.

Escolha um sistema real que você considere agentivo ou possivelmente agentivo. Pode ser ChatGPT, Copilot, Alexa, Waze, um robô aspirador, recomendador, bot, automação residencial, sistema industrial, jogo ou outro sistema relevante.

Analise-o brevemente:

1. Qual é o ambiente?
2. O que o sistema percebe?
3. O que ele pode fazer?
4. Qual objetivo parece orientar seu comportamento?
5. Que decisões pertencem ao próprio sistema?
6. Onde está a autonomia?
7. Você o considera um agente? Justifique.

Não se limite à interface ou ao rótulo comercial. Quando a arquitetura não estiver totalmente visível, declare suas hipóteses: “se a seleção da ação for feita pelo sistema, então...”; “se uma regra fixa controlar o fluxo, então...”. Uma boa análise distingue o que foi observado do que foi inferido.

Termine com a pergunta:

> **Mesmo que esse sistema possa ser considerado um agente, ele precisava ser um agente?**

## A pergunta que fica

Saber reconhecer agência não responde ainda à pergunta de engenharia mais importante. Uma arquitetura pode ser agentiva e, mesmo assim, acrescentar autonomia onde uma solução mais simples seria suficiente.

> **Quando vale a pena tornar um sistema agentivo?**

Essa é a investigação do Encontro 02.
