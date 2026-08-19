---
marp: true
theme: sma
paginate: true
title: Encontro 01 — O que é um agente?
description: Sistemas Multiagentes / Agentic AI
---

<!-- _class: lead -->

# O que é um agente?

Encontro 01 · Sistemas Multiagentes / Agentic AI

<!--
[ESSENCIAL]
O deck completo não precisa ser percorrido linearmente em sala. Permaneça mais tempo em uma discussão produtiva, use respostas como revelação e pule os frames marcados como expansão quando necessário. Não transforme a aula em corrida até o último slide.

Checkpoints flexíveis:
~0–15 min: abertura + resposta individual.
~15–30 min: duplas + critérios + primeiras rupturas.
~30–50 min: termostato + LLM + contraste.
~50–70 min: modelo conceitual + ciclo.
~70–100 min: pedido 381 + if/else + duas lentes + workflow/agente.
~100–110 min: pequena pausa/transição, se necessário.
~110–145 min: casos de fronteira em grupos.
~145–150 min: síntese do tempo conduzido.
Tempo restante: orientação/início do trabalho autônomo.

Abra sem definição. A turma precisará tomar posição e sustentá-la.
-->

---

## Quatro sistemas

<div class="cards">
<div class="card"><strong>A · Termostato</strong><br>Percebe a temperatura e liga ou desliga o aquecimento.</div>
<div class="card"><strong>B · LLM isolada</strong><br>Recebe uma pergunta, produz uma resposta e termina.</div>
<div class="card"><strong>C · Workflow</strong><br>Valida, consulta e envia e-mail por regras predefinidas.</div>
<div class="card"><strong>D · Orientado por objetivo</strong><br>Observa, decide, age e pode decidir novamente.</div>
</div>

<!-- [ESSENCIAL] Apresente os quatro casos sem classificá-los. -->

---
<!-- _class: activity -->

## Quais são agentes?

Para cada sistema, registre:

1. **agente**, **não agente** ou **depende**;
2. uma propriedade que sustentou sua decisão.

<div class="statement">Primeiro: 3 minutos em silêncio.</div>

<!-- [ESSENCIAL] Preserve a resposta individual para comparação posterior. ~0–15 min. -->

---
<!-- _class: question -->

# Qual critério você está usando?

<!-- [ESSENCIAL] Colete critérios antes de projetar a lista seguinte. Depois, peça discussão breve em dupla antes de revelar as primeiras pistas. ~15–30 min. -->

---

## Nossas primeiras pistas

usa IA · conversa · aprende

decide · age sozinho · tem objetivo

inteligência · memória · modernidade

---
<!-- _class: question -->

# Algum desses critérios resolve sozinho?

<!-- Espere previsões e peça um contraexemplo. -->

---

## Uma possível análise

<div class="columns">
<div class="card"><strong>Se linguagem fosse requisito...</strong><br>o termostato nunca apresentaria agência.</div>
<div class="card"><strong>Se usar IA bastasse...</strong><br>toda chamada isolada a uma LLM seria agente.</div>
</div>

<div class="statement">Precisamos explicar responsabilidades, não aparência.</div>

---
<!-- _class: trap -->

## O termostato cria um problema

```text
temperatura percebida = 19 °C
        ↓
temperatura desejada = 22 °C
```

O sistema recebe uma condição do ambiente.

---

## A pequena história

```text
percebe 19 °C
→ compara com 22 °C
→ decide ligar o aquecimento
→ age sobre o ambiente
→ percebe 22 °C
→ decide desligar o aquecimento
```

<!-- [ESSENCIAL] Faça a sequência emergir passo a passo. ~30–50 min. -->

---
<!-- _class: question -->

# Ele usa uma LLM?

---
<!-- _class: takeaway -->

# Não.

O comportamento pode ser simples e determinístico.

---
<!-- _class: question -->

# Ele conversa?

---

## Também não.

Mesmo assim, encontramos:

**percepção · condição desejada · decisão · ação**

---
<!-- _class: takeaway -->

## Primeira ruptura

> **Talvez “usar IA” não seja o que define agência.**

O termostato pode ser um agente simples ou um controlador, conforme o modelo adotado.

Mas IA generativa já não serve como fronteira geral.

<!-- [ESSENCIAL] Transição: “O termostato mostrou que não precisamos de uma LLM. A LLM agora mostrará o problema inverso.” -->

---
<!-- _class: trap -->

## A LLM cria o problema oposto

```text
entrada
  ↓
 LLM
  ↓
saída
```

Linguagem sofisticada. Uma transformação isolada.

<!-- [ESSENCIAL] Não classifique ainda; peça que localizem quem controla a continuidade. -->

---
<!-- _class: question -->

# Quem decide o que acontece depois?

---

## Normalmente, a aplicação externa

- decide **quando chamar**;
- escolhe **o que enviar**;
- determina **o que fazer com a resposta**;
- controla **se haverá próxima etapa**.

---
<!-- _class: takeaway -->

## Segunda ruptura

> **Capacidade cognitiva e agência não são a mesma coisa.**

Uma LLM pode participar da decisão de um agente sem controlar a interação completa.

---
<!-- _class: question -->

## Termostato × LLM isolada

> Qual apresenta mais propriedades de agência nesta arquitetura?

<!-- [ESSENCIAL] Vote antes da análise seguinte. ~30–50 min. -->

---

## Uma possível análise

<div class="columns">
<div class="card"><strong>Termostato</strong><br>Percebe, decide, age e observa novamente.</div>
<div class="card"><strong>LLM isolada</strong><br>Transforma uma entrada; outro componente controla a continuidade.</div>
</div>

<div class="statement">Tecnologia mais sofisticada pode ter menos responsabilidades agentivas.</div>

---
<!-- _class: question -->

# Precisamos de um modelo melhor

Não “quão inteligente parece?”, mas:

> **qual papel exerce na arquitetura?**

<!-- [ESSENCIAL] Transição: “As duas rupturas mostram que aparência não basta. Precisamos localizar responsabilidades.” -->

---
<!-- _class: concept -->

## Ambiente

Aquilo com que o sistema interage e que pode afetar seu comportamento.

<div class="statement">Termostato: espaço, temperatura e equipamento de aquecimento.</div>

---
<!-- _class: concept -->

## Percepção

Informação do ambiente disponível para orientar o comportamento.

```text
condição do espaço → sensor → 19 °C disponíveis ao sistema
```

Perceber não exige um sensor físico: uma resposta de API também pode ser percepção.

---
<!-- _class: concept -->

## Objetivo

A direção que permite avaliar quais ações fazem sentido.

```text
manter a temperatura em 22 °C
```

Não precisa ser inventado pelo sistema nem escrito em linguagem natural.

---
<!-- _class: concept -->

## Decisão

Seleção do que fazer diante das informações disponíveis.

```text
19 °C observados → ligar ou não ligar o aquecimento?
```

Pode usar regras, modelos estatísticos, LLMs ou outros mecanismos.

---
<!-- _class: concept -->

## Ação

Intervenção ou consulta que atravessa a fronteira com o ambiente.

```text
ligar aquecimento · consultar pedido · abrir solicitação
```

---
<!-- _class: concept -->

## Autonomia

Quanto da seleção e continuidade das ações pertence ao sistema.

> Dentro dos limites definidos, **quem determina o próximo passo?**

Autonomia não significa liberdade ilimitada.

---
<!-- _class: concept -->

## Um sistema situado

```text
                     ambiente
              percepção │ ▲ consequência
                        ▼ │
                    ┌─────────┐
        objetivo ──▶│ agente  │
                    │ decisão │
                    └─────────┘
                        │ ação
                        ▼
                     ambiente
```

<!-- [ESSENCIAL] Consolide ambiente, percepção, objetivo, decisão, ação e autonomia. ~50–70 min. -->

---
<!-- _class: trap -->

## O modelo não é uma checklist

> “Se tiver X + Y + Z, então é agente.”

Agência admite **graus**, **fronteiras** e classificações diferentes quando a justificativa é arquiteturalmente consistente.

---

## Uma transformação pode terminar aqui

```text
entrada → transformação → saída
```

Isso pode ser suficiente para o problema.

---
<!-- _class: concept -->

## Agência como ciclo

```text
perceber
   ↓
decidir
   ↓
agir
   ↓
ambiente muda
   ↓
perceber novamente
```

<!-- [ESSENCIAL] Destaque que a consequência da ação alimenta a percepção seguinte. -->

---
<!-- _class: question -->

# O que muda quando existe esse retorno?

---

## A consequência alimenta a próxima decisão

A ação pode:

**falhar · revelar informação · mudar a situação**

O sistema não deve presumir que o ambiente permaneceu igual.

---
<!-- _class: activity -->

## Exemplo trabalhado · pedido 381

**Objetivo**

> Verifique o pedido 381. Se estiver atrasado, abra uma solicitação de atendimento.

<!--
[ESSENCIAL]
Transição: “Até agora classificamos sistemas. Vamos observar uma arquitetura em movimento.”
Proteja este worked example. Se chegar aqui depois de ~80 minutos, reduza discussões anteriores e preserve esta sequência.
-->

---
<!-- _class: question -->

# O que o sistema sabe neste momento?

---

## O que sabe — e o que não sabe

<div class="columns">
<div class="card"><strong>Sabe</strong><br>qual pedido investigar e quando agir.</div>
<div class="card"><strong>Não sabe</strong><br>se o pedido está atrasado.</div>
</div>

Abrir a solicitação agora seria agir sem a informação necessária.

---

## Ações disponíveis

```text
consultar_pedido(id)

abrir_solicitacao(id, motivo)
```

---
<!-- _class: question -->

## O sistema escolhe

```text
consultar_pedido(381)
```

> Percepção, decisão ou ação?

---

## Há decisão e ação

**Decisão:** consultar antes de abrir.

**Ação:** atravessar a fronteira e consultar o ambiente.

```text
“não sei o status” → buscar percepção relevante
```

<div class="statement">A chamada da ferramenta é ação; o retorno alimenta a próxima percepção.</div>

<!-- [ESSENCIAL] Uma consulta pode parecer “percepção”. Decomponha: decidir consultar → agir → receber resposta → perceber. -->

---
<!-- _class: question -->

## O ambiente responde

```text
status = atrasado
```

> O que mudou?

---

## Uma nova percepção ficou disponível

Antes: o sistema conhecia apenas o objetivo.

Agora: sabe que a condição para agir foi satisfeita.

<div class="statement">A resposta do ambiente muda a próxima decisão.</div>

---

## A segunda decisão

```text
abrir_solicitacao(381, "pedido atrasado")
```

A nova percepção sustenta a escolha; a ação altera o ambiente.

---
<!-- _class: question -->

## O ambiente confirma

```text
solicitação criada
```

> Por que essa confirmação importa?

---

## A confirmação também é percepção

Ela informa que a ação produziu o efeito esperado.

```text
se retornasse “serviço indisponível”
→ a situação exigiria outra decisão
```

---
<!-- _class: synthesis -->

## Reconstruindo o pedido 381

```text
objetivo
→ decisão: consultar
→ ação: consultar_pedido(381)
→ percepção: status = atrasado
→ decisão: abrir solicitação
→ ação: abrir_solicitacao(...)
→ percepção: solicitação criada
```

<!-- [ESSENCIAL] Só avance quando a turma conseguir localizar cada responsabilidade. -->

---
<!-- _class: question -->

# Onde exatamente estava a decisão?

---

## Em duas seleções sustentadas pelo que se sabia

1. consultar, porque faltava o status;
2. abrir, porque o ambiente informou atraso.

> A saída final não mostra sozinha como essas responsabilidades foram distribuídas.

---
<!-- _class: question -->

# E se fosse tudo `if/else`?

Isso eliminaria automaticamente a agência?

<!-- [ESSENCIAL] Transição: “Localizamos decisões; agora precisamos perguntar se o mecanismo que as implementa muda a classificação.” -->

---

## Software determinístico também percebe e age

O termostato já mostrou isso.

```text
se temperatura < desejada
→ ligar aquecimento
```

Uma regra é um mecanismo possível de decisão.

---

## Mas regras podem fixar toda a trajetória

```text
consultar
→ se atrasado, abrir
→ senão, encerrar
```

Nesse caso, o espaço de escolha pode ser muito limitado.

---
<!-- _class: trap -->

## Armadilha

> **`if/else` não decide sozinho se algo é agente.**

Precisamos observar:

**onde há escolha · quem controla o próximo passo · quanto já foi predeterminado**

<!-- [ESSENCIAL] Não aceite a regra simplista `if/else = não agente`. -->

---

## Duas lentes para “agente”

O termo é usado com **granularidades diferentes**.

Não precisamos escolher uma lente como certa e a outra como errada.

<!-- [ESSENCIAL] Transição: “O `if/else` revelou que estamos usando a palavra agente com granularidades diferentes.” -->

---
<!-- _class: concept -->

## Sistemas Multiagentes · lente ampla

```text
situado em ambiente
→ percebe
→ age
→ possui condição orientadora
→ opera com algum grau de autonomia
```

Sistemas simples e determinísticos podem apresentar agência.

---
<!-- _class: concept -->

## Agentic AI · lente de engenharia

Em sistemas baseados em LLMs, perguntamos:

> **Quem controla a trajetória?**

> **Quem escolhe o próximo passo diante do estado observado?**

<div class="statement">Nesta disciplina precisaremos das duas lentes.</div>

<!-- [ESSENCIAL] A lente ampla reconhece propriedades; a lente de engenharia ajuda a organizar o controle. Nenhuma invalida a outra. -->

---

## LLM isolada

```text
texto → LLM → resumo
```

Outro componente controla quando chamar e o que fazer depois.

---

## Workflow

```text
validar → consultar → enviar
```

O fluxo determina previamente o próximo passo ou ramo.

---

## Agente

```text
objetivo + percepção
→ escolher entre ações permitidas
→ observar consequência
```

Existe algum espaço de decisão orientado pelo objetivo.

---
<!-- _class: takeaway -->

## LLM não está no mesmo eixo

```text
LLM = capacidade / componente possível

workflow ↔ agente = organização do controle
```

---

## As combinações são possíveis

<div class="cards">
<div class="card"><strong>Workflow</strong><br>sem LLM</div>
<div class="card"><strong>Workflow</strong><br>com LLM</div>
<div class="card"><strong>Agente</strong><br>com LLM</div>
<div class="card"><strong>Agente</strong><br>sem LLM</div>
</div>

<div class="statement">A presença de uma LLM não determina a arquitetura.</div>

<!-- [ESSENCIAL] Transição: “Agora podemos separar capacidade usada de organização do controle.” ~70–100 min. -->

---
<!-- _class: lead -->

# O que não é requisito?

Vamos desmontar alguns atalhos.

<!-- [EXPANSÃO] Acelere este bloco se os contraexemplos já estiverem claros; mantenha-o para estudo posterior. -->

---
<!-- _class: question -->

# Precisa usar IA generativa?

---
<!-- _class: takeaway -->

## Não.

O termostato já mostrou percepção, objetivo, decisão e ação sem IA generativa.

Uma LLM é um mecanismo possível, não um requisito.

---
<!-- _class: question -->

# Precisa conversar?

---

## Não.

Robôs, controladores e sistemas de software podem perceber e agir sem interface conversacional.

Um chatbot pode conversar sem controlar outra ação além de produzir texto.

---
<!-- _class: question -->

# Precisa aprender?

---

## Não.

Regras fixas podem sustentar interação autônoma com o ambiente.

Aprender pode mudar a decisão ao longo do tempo; não é condição necessária para agência.

---
<!-- _class: question -->

# Precisa ter memória complexa?

---

## Não.

A informação relevante precisa estar disponível para a decisão corrente.

Isso não exige uma arquitetura sofisticada de memória.

---
<!-- _class: question -->

# Precisa ser sofisticado?

---

## Não.

Um sistema simples pode assumir responsabilidades agentivas estreitas.

Um sistema sofisticado pode executar apenas uma transformação comandada externamente.

---
<!-- _class: question -->

# Precisa ser imprevisível?

---

## Não.

Determinismo não elimina percepção e ação.

Aleatoriedade não cria objetivo nem autonomia.

---
<!-- _class: activity -->

## Casos de fronteira

Para cada caso:

1. classifique;
2. identifique a propriedade decisiva;
3. aceite `depende` somente se explicar **do que depende**.

<!--
[ESSENCIAL]
~110–145 min. Divida a turma em grupos pequenos; cada grupo recebe um caso diferente. Dê 8–10 minutos para preparar uma defesa de ~90 segundos. Permita uma contestação curta e só então revele a análise correspondente no deck. Não é seminário: nem todos precisam apresentar todos os casos. Com muitos grupos, repita casos ou use um subconjunto. Se o terceiro tempo estiver apertado, use apenas 3 casos.
-->

---
<!-- _class: question -->

## Chatbot simples

```text
mensagem → resposta
```

Isso basta para chamá-lo de agente?

<!-- Não revele a análise antes da defesa do grupo responsável. -->

---

## Depende da arquitetura

Só responder aproxima o caso de uma transformação isolada.

Se puder escolher entre responder, pedir informação e agir externamente, a análise muda.

---
<!-- _class: question -->

## Robô aspirador

Percebe obstáculos, muda de direção e continua limpando.

> Onde está sua autonomia?

---

## Uma possível análise

Sensores percebem o espaço; mover e aspirar são ações; limpar orienta o comportamento.

Mesmo com regras, o próximo movimento depende do ambiente percebido.

---
<!-- _class: question -->

## Workflow de aprovação

Encaminha ao gestor, espera a resposta e, se aprovada, envia ao financeiro.

> Percepção e ação bastam?

---

## O ponto decisivo

O fluxo completo e seus ramos podem já determinar cada etapa.

Há percepção e ação, mas pouca autonomia se o sistema apenas executa a trajetória especificada.

---
<!-- _class: question -->

## LLM com capacidade externa

Pode consultar um cadastro e enviar mensagens.

> Ter capacidades basta?

---

## Precisamos saber quem seleciona a ação

Se outro programa sempre manda consultar e enviar, há um workflow.

Se o sistema escolhe capacidades conforme objetivo e percepções, assume mais responsabilidade.

---
<!-- _class: question -->

## API escolhida por regra fixa

A regra escolhe a API; a LLM apenas transforma o resultado em linguagem.

> Agente, workflow ou depende?

<div class="statement">Vote antes de discutir.</div>

<!--
[ESSENCIAL]
Peer Instruction: 1) voto individual; 2) registrar justificativa; 3) discutir em dupla; 4) novo voto; 5) revelar a análise seguinte. Não sinalize a resposta preferida.
-->

---
<!-- _class: activity -->

## Compare as justificativas

> **Converse com alguém que respondeu diferente.**

Depois, **vote novamente**.

<!-- [ESSENCIAL] Peça que identifiquem o argumento que mudou ou fortaleceu a posição. -->

---

## Uma classificação bem sustentada

**Workflow com componente de LLM:** a regra escolhe a ação e a LLM não controla o próximo passo.

Outro rótulo exige explicar qual autonomia pertence ao sistema completo.

---
<!-- _class: takeaway -->

## Casos de fronteira não exigem unanimidade

> **Classificações podem divergir; a qualidade da justificativa é o que importa.**

“Tem IA”, “conversa” ou “usa API” não bastam.

<!-- [ESSENCIAL] Transição: “Os casos divergiram, mas o vocabulário das justificativas ficou mais preciso. Vamos reconstruir o que mudou.” -->

---
<!-- _class: lead -->

# Verifique sua compreensão

Agora o modelo precisa funcionar em casos novos.

<!-- [EXPANSÃO] Use se houver tempo, como recuperação ou em estudo posterior. Os oito frames seguintes formam quatro pares pergunta–análise. -->

---
<!-- _class: question -->

## 1 · Irrigação da estufa

Lê a umidade a cada dez minutos. Abaixo do limite, abre a válvula por dois minutos e volta a medir.

> Localize ambiente, percepção, objetivo, decisão, ação e autonomia.

<!-- [EXPANSÃO] Espere uma resposta antes de revelar a análise. -->

---

## Análise · irrigação

**Ambiente:** solo, água e válvula · **Percepção:** umidade

**Objetivo:** manter o limite · **Decisão:** abrir ou não

**Ação:** abrir a válvula · **Autonomia:** repetir o ciclo sem nova ordem externa

<!-- [EXPANSÃO] -->

---
<!-- _class: question -->

## 2 · Gerador de parecer

Um clique envia um documento à LLM, recebe o parecer e o exibe. Nada mais é consultado ou executado.

> Por que a presença da LLM não basta para concluir “agente”?

<!-- [EXPANSÃO] Espere uma resposta antes de revelar a análise. -->

---

## Análise · parecer

O clique inicia uma transformação isolada.

A arquitetura não atribui ao modelo a escolha de quando agir, o que consultar depois ou como produzir outros efeitos.

<!-- [EXPANSÃO] -->

---
<!-- _class: question -->

## 3 · Monitor de estoque

Recebe “reduzir faltas”, mas uma regra fixa a ordem das consultas e calcula a compra. A LLM apenas redige a justificativa.

> Quem possui a responsabilidade decisiva?

<!-- [EXPANSÃO] Espere uma resposta antes de revelar a análise. -->

---

## Análise · estoque

A regra externa controla a trajetória e calcula a ação.

A LLM não passa a decidir porque redige a justificativa.

<div class="statement">Workflow é uma classificação bem sustentada.</div>

<!-- [EXPANSÃO] -->

---
<!-- _class: question -->

## 4 · Mesma saída, arquiteturas diferentes

Um fluxo fixo e um sistema orientado por objetivo abrem a mesma solicitação.

> Por que a saída final não prova o mesmo grau de agência?

<!-- [EXPANSÃO] Espere uma resposta antes de revelar a análise. -->

---

## Análise · mesma saída

O primeiro recebe o caminho completo.

O segundo seleciona o próximo passo entre possibilidades, conforme objetivo e percepções.

> A saída apaga as decisões que produziram o resultado.

<!-- [EXPANSÃO] -->

---
<!-- _class: synthesis -->

## Começamos com uma intuição

> “Agente parece ser algo inteligente.”

<!-- [ESSENCIAL] ~145–150 min. Reconstrua rapidamente as rupturas, sem reexplicar cada bloco. -->

---
<!-- _class: synthesis -->

## O termostato quebrou essa intuição

Sem conversar ou usar IA generativa, apresentou:

**percepção · condição desejada · decisão · ação · retorno**

---
<!-- _class: synthesis -->

## A LLM mostrou o problema oposto

Linguagem sofisticada não atribui automaticamente controle sobre:

**continuidade · ações · consequências**

---
<!-- _class: synthesis -->

## Então mudamos a pergunta

Não:

> quão inteligente parece?

Mas:

> **qual papel exerce na arquitetura?**

---
<!-- _class: synthesis -->

## Nosso modelo de análise

```text
ambiente → percepção → decisão → ação → consequência
                ↑         ↑
             objetivo  autonomia
```

---
<!-- _class: takeaway -->

## Três ideias para levar

**Uma LLM não é automaticamente um agente.**

**Um agente não precisa usar IA generativa.**

**Responsabilidades e autonomia importam mais que o rótulo isolado.**

<!-- [ESSENCIAL] Retome uma classificação da abertura e peça uma justificativa agora mais precisa. -->

---
<!-- _class: activity -->

## Trabalho autônomo orientado

Escolha **um sistema real** possivelmente agentivo.

Pode ser assistente, navegador, robô, recomendador, bot, automação, sistema industrial ou jogo.

**Formativo · sem nota · laboratório OU casa · durante a semana**

Conclua antes do próximo encontro; o resultado será retomado no Encontro 02.

<!-- [ESSENCIAL] Tempo restante: oriente e, se possível, deixe a turma iniciar. -->

---
<!-- _class: activity -->

## Analise o sistema

1. Qual é o ambiente? O que percebe?
2. O que pode fazer? Qual objetivo o orienta?
3. Que decisões pertencem ao sistema?
4. Onde está a autonomia?
5. Você o considera agente? **Justifique.**

---
<!-- _class: activity -->

## Quando a arquitetura não estiver visível

Declare suas hipóteses:

> “Se o sistema seleciona a ação, então...”

> “Se uma regra fixa controla o fluxo, então...”

Termine perguntando: **mesmo que seja agente, precisava ser?**

---
<!-- _class: lead -->

# Ele precisava ser um agente?

Encontro 02 · **Quando vale a pena tornar um sistema agentivo?**

<!-- [ESSENCIAL] Encerre com a dúvida; não antecipe a resposta do próximo encontro. -->
