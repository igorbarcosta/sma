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
Abra sem definição. Diga apenas que a turma precisará tomar posição e sustentá-la.
-->

---

## Quatro sistemas estranhos

<div class="cards">
<div class="card"><strong>A · Termostato</strong><br>Percebe a temperatura e liga ou desliga o aquecimento.</div>
<div class="card"><strong>B · Chamada à LLM</strong><br>Recebe uma pergunta, gera uma resposta e termina.</div>
<div class="card"><strong>C · Workflow</strong><br>Valida, consulta e envia e-mail por regras predefinidas.</div>
<div class="card"><strong>D · Orientado por objetivo</strong><br>Observa, decide, age e pode decidir novamente.</div>
</div>

<!--
Leia somente o necessário. Não explique nem classifique os casos.
-->

---
<!-- _class: activity -->

## Quais são agentes?

Para cada sistema, registre:

1. **agente**, **não agente** ou **depende / não tenho certeza**;
2. ao menos **uma propriedade** usada na decisão.

<div class="statement">Primeiro: 3 minutos em silêncio.</div>

<!--
Garanta uma resposta individual antes de qualquer fala coletiva. Circule e observe quais critérios aparecem.
-->

---
<!-- _class: activity -->

## Tente convencer seu colega

Compare as quatro classificações.

Se alguém mudar de opinião, registrem:

> **Qual argumento provocou a mudança?**

<!--
Discussão em dupla por 4–5 minutos. Peça que preservem a resposta inicial para comparação posterior.
-->

---
<!-- _class: question -->

## Que critérios usamos sem perceber?

IA · conversa · inteligência · autonomia · decisão

percepção · ação · aprendizagem · objetivo · memória

<!--
Registre no quadro os critérios que realmente surgirem. Não valide requisitos ainda. Pergunte por contradições entre as classificações e os critérios.
-->

---
<!-- _class: trap -->

## O termostato cria um problema

Não conversa · não usa LLM · não aprende

Mas percebe a temperatura, decide entre possibilidades e age para manter uma condição desejada.

> IA moderna pode ser nosso critério?

<!--
Use o termostato como contraexemplo, sem encerrar sua classificação. Faça emergir que inteligência generativa não pode ser o critério principal.
-->

---
<!-- _class: question -->

# Então uma LLM é um agente?

<!--
Espere. Colete duas ou três justificativas antes de mostrar as arquiteturas. Não aceite apenas sim/não: peça a propriedade decisiva.
-->

---

## A LLM cria o problema oposto

<div class="columns">
<div>

```text
entrada
  ↓
 LLM
  ↓
saída
```

</div>
<div>

Quem controla:

quando chamar? · o que acontece depois?

se haverá outra ação? · quais efeitos ocorrerão?

</div>
</div>

<!--
Mostre que linguagem sofisticada não atribui automaticamente à LLM a responsabilidade pela continuidade ou pelos efeitos da interação.
-->

---
<!-- _class: takeaway -->

## O contraste

Uma LLM pode fazer parte do mecanismo de **decisão** de um agente.

<div class="statement">Uma LLM não é automaticamente um agente.</div>

Um agente não precisa utilizar IA generativa.

<!--
Faça a transição: os dois contraexemplos exigem um modelo que localize responsabilidades na arquitetura.
-->

---
<!-- _class: question -->

## O que nosso modelo precisa explicar?

> Por que sistemas parecidos receberam classificações diferentes?

> Por que sistemas tão diferentes receberam a mesma classificação?

<!--
Use o conflito criado pela turma para justificar a formalização. Não apresente o modelo como mera definição para memorizar.
-->

---
<!-- _class: concept -->

## Um sistema situado

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

<!--
Construa o desenho aos poucos no quadro. Comece pelo ambiente; pergunte o que atravessa cada fronteira antes de nomear percepção e ação.
-->

---
<!-- _class: concept -->

## O ciclo muda o que vem depois

```text
perceber → decidir → agir
   ↑                   │
   └── consequência ───┘
```

O comportamento é orientado por um **objetivo** e possui algum grau de **autonomia**.

<!--
Explique em até 5 minutos. Destaque que uma ação altera ou consulta o ambiente e produz nova informação para a próxima decisão.
-->

---
<!-- _class: concept -->

## Dimensões para analisar

<div class="cards">
<div class="card"><strong>Ambiente</strong><br>Com o que o sistema interage?</div>
<div class="card"><strong>Percepção</strong><br>Que informação ele obtém?</div>
<div class="card"><strong>Ação</strong><br>O que ele pode alterar?</div>
<div class="card"><strong>Objetivo</strong><br>O que orienta o comportamento?</div>
<div class="card"><strong>Decisão</strong><br>Que escolha ocorre?</div>
<div class="card"><strong>Autonomia</strong><br>Que escolhas pertencem ao sistema?</div>
</div>

<!--
Use como linguagem de análise, não como seis caixas obrigatórias. Evite aprofundar estado, memória ou planejamento.
-->

---
<!-- _class: trap -->

## Não é uma fórmula

> “Se tiver X + Y + Z, então é agente.”

Agência admite **graus**, **fronteiras** e classificações diferentes quando a argumentação é tecnicamente consistente.

<!--
Erro comum: trocar o critério superficial por uma checklist igualmente superficial. Peça um exemplo em que o grau de autonomia seja discutível.
-->

---
<!-- _class: activity -->

## Simulação: pedido 381

**Objetivo**

> Verifique o pedido 381. Se estiver atrasado, abra uma solicitação de atendimento.

**Ações disponíveis**

```text
consultar_pedido(id)
abrir_solicitacao(id, motivo)
```

<!--
Escolha uma pessoa para representar o agente; o professor ou cartões representam o ambiente. Não fale em tool calling ou SDK.
-->

---
<!-- _class: activity -->

## O agente escolhe uma ação

```text
consultar_pedido(381)
```

**Ambiente responde:**

```text
status = atrasado
```

> O que acabou de acontecer?

<!--
Pause antes da resposta do ambiente. Pergunte por que consultar veio antes de abrir a solicitação. Depois revele o status.
-->

---
<!-- _class: activity -->

## O novo estado muda a decisão

```text
abrir_solicitacao(381, "pedido atrasado")
```

**Ambiente responde:**

```text
solicitação criada
```

<!--
Peça que a turma indique qual informação sustentou a segunda escolha. Destaque a observação da consequência sem antecipar mecanismos internos.
-->

---
<!-- _class: question -->

## Onde ocorreu cada responsabilidade?

Percepção? · Decisão? · Ação?

Ambiente? · Objetivo? · Autonomia?

> E se todas as etapas fossem determinadas previamente por `if/else`?

<!--
Construa a resposta coletivamente. A presença de if/else não encerra a discussão: diferencie decisão arquitetural, liberdade de seleção e regras fixas.
-->

---
<!-- _class: question -->

## Agente, workflow ou depende?

> Um assistente recebe um pedido. Uma regra fixa determina qual API será chamada. A LLM apenas transforma o resultado em linguagem natural.

<!--
Peer Instruction. Exija voto individual antes da conversa. Opções: agente; workflow; depende. Não sinalize uma resposta preferida.
-->

---
<!-- _class: activity -->

## Vote → discuta → vote novamente

1. Escolha uma classificação.
2. Registre a propriedade decisiva.
3. Tente convencer um colega.
4. Vote novamente.

> Sua justificativa ficou melhor, mesmo se seu voto não mudou?

<!--
Reserve 6–8 minutos. Compare justificativas, não apenas a distribuição dos votos. Evidência desejada: vocabulário arquitetural mais preciso no segundo voto.
-->

---
<!-- _class: activity -->

## Desafio de fronteira

Cada grupo recebe um sistema:

termostato · robô aspirador · chatbot simples

workflow de aprovação · LLM com capacidade externa

agente de compras orientado por objetivo

<!--
Terceiro tempo. Distribua um caso por grupo. Trabalho de análise: 12 minutos. Não peça pesquisa externa; as descrições podem ser complementadas oralmente.
-->

---
<!-- _class: activity -->

## Prepare uma defesa curta

> Nosso sistema apresenta estas propriedades de agência e não apresenta estas outras. Por isso, nossa classificação é...

**A turma poderá contestar.**

<!--
Apresentações de até 90 segundos. Limite a uma contestação curta por grupo para evitar formato de seminário.
-->

---
<!-- _class: question -->

## Coloque a defesa à prova

Isso é decisão ou condição programada? · Onde está o ambiente?

O sistema poderia não agir? · Aprender é requisito?

Sem a LLM, ainda é agente? · Onde termina a autonomia?

<!--
Escolha perguntas conforme a fragilidade real de cada defesa. Não use todas com todos os grupos.
-->

---
<!-- _class: synthesis -->

## Três ideias para levar

**Uma LLM não é automaticamente um agente.**

**Um agente não precisa usar IA generativa.**

**Responsabilidades, decisões e graus de autonomia importam mais que o rótulo isolado.**

<!--
Retome duas classificações do início e peça que a turma as reformule com o novo modelo. Isso fornece a evidência final de mudança de critério.
-->

---
<!-- _class: activity -->

## Trabalho autônomo orientado

Escolha **um sistema real** possivelmente agentivo.

Analise ambiente · percepção · ação · objetivo · decisão · autonomia.

Classifique e justifique.

**Formativo · sem nota · laboratório OU casa · durante a semana**

<!--
Mostre a página do encontro para as sete perguntas completas. Reforce que não é Desafio nem avaliação e que será retomado brevemente no próximo encontro.
-->

---
<!-- _class: lead -->

# Ele precisava ser um agente?

Próximo encontro: **quando vale a pena tornar um sistema agentivo?**

<!--
Encerre com a dúvida, sem respondê-la. Essa pergunta deve orientar a transferência no trabalho autônomo.
-->
