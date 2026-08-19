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

<!-- Abra sem definição. A turma precisará tomar posição e sustentá-la. -->

---

## Quatro sistemas

<div class="cards">
<div class="card"><strong>A · Termostato</strong><br>Percebe a temperatura e liga ou desliga o aquecimento.</div>
<div class="card"><strong>B · LLM isolada</strong><br>Recebe uma pergunta, produz uma resposta e termina.</div>
<div class="card"><strong>C · Workflow</strong><br>Valida, consulta e envia e-mail por regras predefinidas.</div>
<div class="card"><strong>D · Orientado por objetivo</strong><br>Observa, decide, age e pode decidir novamente.</div>
</div>

---
<!-- _class: activity -->

## Quais são agentes?

Para cada sistema, registre:

1. **agente**, **não agente** ou **depende**;
2. uma propriedade que sustentou sua decisão.

<div class="statement">Primeiro: 3 minutos em silêncio.</div>

<!-- Preserve a resposta individual para comparação posterior. -->

---
<!-- _class: question -->

# Qual critério você está usando?

<!-- Colete critérios antes de projetar a lista seguinte. -->

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
temperatura = 28 °C
        ↓
desejada = 23 °C
```

O sistema recebe uma condição do ambiente.

---

## A pequena história

```text
percebe 28 °C
→ compara com 23 °C
→ decide ligar o resfriamento
→ age sobre o ambiente
→ percebe novamente
```

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

<!-- Vote antes da análise seguinte. -->

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

---
<!-- _class: concept -->

## Ambiente

Aquilo com que o sistema interage e que pode afetar seu comportamento.

<div class="statement">Termostato: espaço, temperatura e equipamento de climatização.</div>

---
<!-- _class: concept -->

## Percepção

Informação do ambiente disponível para orientar o comportamento.

```text
condição do espaço → sensor → 28 °C disponíveis ao sistema
```

Perceber não exige um sensor físico: uma resposta de API também pode ser percepção.

---
<!-- _class: concept -->

## Objetivo

A direção que permite avaliar quais ações fazem sentido.

```text
manter a temperatura em 23 °C
```

Não precisa ser inventado pelo sistema nem escrito em linguagem natural.

---
<!-- _class: concept -->

## Decisão

Seleção do que fazer diante das informações disponíveis.

```text
28 °C observados → ligar ou não ligar?
```

Pode usar regras, modelos estatísticos, LLMs ou outros mecanismos.

---
<!-- _class: concept -->

## Ação

Intervenção ou consulta que atravessa a fronteira com o ambiente.

```text
ligar resfriamento · consultar pedido · abrir solicitação
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

---

## Software determinístico também percebe e age

O termostato já mostrou isso.

```text
se temperatura > desejada
→ ligar resfriamento
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

## Não é uma taxonomia absoluta

<div class="cards">
<div class="card"><strong>LLM</strong><br>capacidade possível</div>
<div class="card"><strong>Workflow</strong><br>trajetória especificada</div>
<div class="card"><strong>Agente</strong><br>espaço de decisão orientado</div>
</div>

<div class="statement">A presença de uma LLM não determina a arquitetura.</div>

---
<!-- _class: lead -->

# O que não é requisito?

Vamos desmontar alguns atalhos.

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

---
<!-- _class: question -->

## Chatbot simples

```text
mensagem → resposta
```

Isso basta para chamá-lo de agente?

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

---

## Uma classificação bem sustentada

**Workflow com componente de LLM:** a regra escolhe a ação e a LLM não controla o próximo passo.

Outro rótulo exige explicar qual autonomia pertence ao sistema completo.

---
<!-- _class: takeaway -->

## Casos de fronteira não exigem unanimidade

> **Classificações podem divergir; a qualidade da justificativa é o que importa.**

“Tem IA”, “conversa” ou “usa API” não bastam.

---
<!-- _class: lead -->

# Verifique sua compreensão

Agora o modelo precisa funcionar em casos novos.

---
<!-- _class: question -->

## 1 · Irrigação da estufa

Lê a umidade a cada dez minutos. Abaixo do limite, abre a válvula por dois minutos e volta a medir.

> Localize ambiente, percepção, objetivo, decisão, ação e autonomia.

---

## Análise · irrigação

**Ambiente:** solo, água e válvula · **Percepção:** umidade

**Objetivo:** manter o limite · **Decisão:** abrir ou não

**Ação:** abrir a válvula · **Autonomia:** repetir o ciclo sem nova ordem externa

---
<!-- _class: question -->

## 2 · Gerador de parecer

Um clique envia um documento à LLM, recebe o parecer e o exibe. Nada mais é consultado ou executado.

> Por que a presença da LLM não basta para concluir “agente”?

---

## Análise · parecer

O clique inicia uma transformação isolada.

A arquitetura não atribui ao modelo a escolha de quando agir, o que consultar depois ou como produzir outros efeitos.

---
<!-- _class: question -->

## 3 · Monitor de estoque

Recebe “reduzir faltas”, mas uma regra fixa a ordem das consultas e calcula a compra. A LLM apenas redige a justificativa.

> Quem possui a responsabilidade decisiva?

---

## Análise · estoque

A regra externa controla a trajetória e calcula a ação.

A LLM não passa a decidir porque redige a justificativa.

<div class="statement">Workflow é uma classificação bem sustentada.</div>

---
<!-- _class: question -->

## 4 · Mesma saída, arquiteturas diferentes

Um fluxo fixo e um sistema orientado por objetivo abrem a mesma solicitação.

> Por que a saída final não prova o mesmo grau de agência?

---

## Análise · mesma saída

O primeiro recebe o caminho completo.

O segundo seleciona o próximo passo entre possibilidades, conforme objetivo e percepções.

> A saída apaga as decisões que produziram o resultado.

---
<!-- _class: synthesis -->

## Começamos com uma intuição

> “Agente parece ser algo inteligente.”

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

---
<!-- _class: activity -->

## Trabalho autônomo orientado

Escolha **um sistema real** possivelmente agentivo.

Pode ser assistente, navegador, robô, recomendador, bot, automação, sistema industrial ou jogo.

**Formativo · sem nota · laboratório OU casa · durante a semana**

Conclua antes do próximo encontro; o resultado será retomado no Encontro 02.

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

<!-- Encerre com a dúvida; não antecipe a resposta do próximo encontro. -->
