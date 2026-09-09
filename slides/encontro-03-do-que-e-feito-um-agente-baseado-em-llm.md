---
marp: true
theme: sma
paginate: true
title: Encontro 03 — Do que é feito um agente baseado em LLM?
description: Sistemas Multiagentes / Agentic AI
---

<!-- _class: lead -->

# Do que é feito um agente baseado em LLM?

Encontro 03 · Sistemas Multiagentes / Agentic AI

<!--
[ESSENCIAL]
Checkpoints flexíveis:
~0–10 min: retomada + resposta isolada.
~10–45 min: executar e observar o ciclo controlado.
~45–80 min: formalizar responsabilidades.
~80–115 min: diagnosticar as duas versões defeituosas.
~115–140 min: LLM sob limites + comparação.
~140–155 min: síntese.
Tempo restante: orientação e início do trabalho autônomo.

Abra pelo problema da continuidade. Não comece definindo componentes.
-->

---

## Do encontro anterior

```text
objetivo + estado + ações permitidas
                 ↓
              decisão
```

O CampusBot já escolhia parte da trajetória em tempo de execução.

<div class="statement">Mas quem sustenta a trajetória depois da primeira escolha?</div>

<!-- [ESSENCIAL] Recupere rapidamente a ideia de que LLM e controle da trajetória não são sinônimos. -->

---
<!-- _class: question -->

# Uma boa resposta já basta?

---

<!-- _class: activity -->

## Execute uma resposta isolada

```bash
uv run python praticas/encontro-03/01_uma_resposta.py
```

<div class="statement">Leia a saída. Ainda não explique a arquitetura.</div>

<!-- [ESSENCIAL] Peça execução logo no início. ~0–10 min. -->

---

## Uma pessoa escreve

> “O projetor não funciona e a apresentação começa em breve.”

```text
entrada → LLM ou função → resposta
```

---
<!-- _class: question -->

## O que falta para ela continuar ajudando?

- Qual objetivo orientou a resposta?
- Que informação ainda precisa ser obtida?
- Quem escolhe o próximo passo?
- Como o sistema sabe que terminou?

<!-- [ESSENCIAL] Primeiro, respostas individuais curtas. Não busque uma lista perfeita. -->

---

## Uma possível análise

<div class="cards">
<div class="card"><strong>Resposta isolada</strong><br>Pode ser útil e bem escrita.</div>
<div class="card"><strong>Trajetória</strong><br>Ainda não declara estado, próxima decisão ou parada.</div>
</div>

<div class="statement">O problema não é a qualidade do texto. É a responsabilidade de controle que não está visível.</div>

---
<!-- _class: takeaway -->

# Uma LLM pode responder.

# Isso não basta, por si só, para organizar uma sequência de decisões.

---

<!-- _class: activity -->

## Agora faça a conversa virar um ciclo

Antes de executar, preveja:

> Qual deve ser a primeira escolha para o caso do projetor?

```bash
uv run python praticas/encontro-03/02_ciclo_controlado.py
```

<!-- [ESSENCIAL] Dê um minuto para previsão. Depois acompanhe a execução em conjunto. ~10–45 min. -->

---

## Percepção inicial

```text
O projetor não funciona e a apresentação começa em breve.
```

```text
estado = { local: ?, problema: projetor, urgente: sim }
```

---

## Primeira decisão

```text
ação: perguntar_local
motivo: o local é necessário para orientar o próximo passo
```

> “Em qual local isso está acontecendo?”

---

## O interlocutor responde

```text
É no Lab 4.
```

Isso é uma **nova percepção**.

---

## O estado muda

```text
antes  local = ?
depois local = Lab 4
```

<div class="statement">A segunda decisão poderá usar algo que não estava disponível na primeira.</div>

---

## Segunda decisão

```text
ação: orientar_e_encerrar
motivo: o agente reuniu a informação necessária,
        mas seu limite é conversacional
```

---
<!-- _class: question -->

# Por que ele não abre um chamado?

---
<!-- _class: trap -->

## Porque ele ainda não possui essa capacidade

```text
“Chamado aberto.”
```

seria apenas texto, não uma ação verificada no ambiente.

<div class="statement">Neste encontro: ciclo e responsabilidades. No próximo: ferramentas e ação externa.</div>

---

## O ciclo que acabamos de observar

```text
objetivo
  ↓
percepção → estado → decisão → próximo passo
     ↑                         ↓
interlocutor ← controlador ← validação / parada
```

<!-- [ESSENCIAL] Aponte cada elemento na execução anterior. Não apresente como checklist abstrato. -->

---
<!-- _class: concept -->

## Objetivo e limites

```text
ajudar com o problema do projetor
sem inventar uma ação externa
```

> **O que o sistema tenta alcançar — e o que não pode alegar fazer?**

---
<!-- _class: concept -->

## Percepção

```text
mensagem inicial
nova resposta da pessoa
```

> **O que acabou de ficar conhecido?**

---
<!-- _class: concept -->

## Estado de execução

```text
local = Lab 4
problema = projetor
urgente = sim
```

> **O que o sistema precisa conservar para a próxima decisão?**

---
<!-- _class: concept -->

## Modelo de decisão

```text
objetivo + percepção + estado
               ↓
        próximo passo
```

Ele pode ser uma LLM, uma regra ou outro mecanismo.

> **Diante do que sei, o que faz sentido fazer agora?**

---
<!-- _class: concept -->

## Ações permitidas

```text
perguntar o local
orientar e encerrar
```

O conjunto é pequeno de propósito.

> **O que este agente pode realmente escolher?**

---
<!-- _class: concept -->

## Controlador do ciclo

```text
entrega informações
→ valida a decisão
→ obtém nova percepção ou encerra
```

> **Quem mantém a execução coerente entre uma decisão e outra?**

---
<!-- _class: concept -->

## Condição de parada

```text
concluiu = verdadeiro
```

ou

```text
limite de passos atingido
```

> **Quando o sistema deve deixar de agir?**

---
<!-- _class: takeaway -->

## Componentes não são sinônimos

<div class="columns">
<div class="card"><strong>LLM</strong><br>pode propor uma decisão</div>
<div class="card"><strong>Controlador</strong><br>organiza o ciclo e seus limites</div>
</div>

<div class="statement">Uma biblioteca pode juntar responsabilidades; isso não apaga as perguntas arquiteturais.</div>

---
<!-- _class: question -->

# E se uma responsabilidade falhar?

---
<!-- _class: activity -->

## Desligue o estado de propósito

Preveja o passo seguinte depois de a pessoa informar “É no Lab 4”.

```bash
uv run python praticas/encontro-03/03_diagnosticar_o_ciclo.py --sem-estado
```

<!-- [ESSENCIAL] Peça previsão; só então execute. ~80–100 min. -->

---

## Registro da versão defeituosa

```text
NOVA PERCEPÇÃO: É no Lab 4.
ESTADO ATUAL: local = ?

PASSO 2
DECISÃO: perguntar_local
```

O agente pergunta de novo.

---
<!-- _class: question -->

# A LLM “esqueceu”?

---

## Análise do diagnóstico

Não precisamos atribuir o problema genericamente ao modelo.

```text
percepção ocorreu
      ↓
estado não foi atualizado
      ↓
decisão seguinte não recebeu a informação
```

<div class="statement">A falha está na passagem entre percepção e estado.</div>

---
<!-- _class: activity -->

## Agora interrompa um ciclo que funciona

```bash
uv run python praticas/encontro-03/03_diagnosticar_o_ciclo.py --limite 1
```

> Ele deveria ter terminado depois de uma única decisão?

---

## Registro da outra falha

```text
PASSO 1: perguntar local
NOVA PERCEPÇÃO: É no Lab 4.

PARADA DE SEGURANÇA: limite de passos atingido
```

O agente recebeu a informação necessária, mas não pôde usá-la.

---
<!-- _class: takeaway -->

## Limites de passos não demonstram inteligência

Eles são um mecanismo de controle.

```text
sem limite → o ciclo pode repetir indefinidamente
limite inadequado → o ciclo pode parar cedo demais
```

---
<!-- _class: trap -->

## Estado não é, ainda, “memória” em sentido completo

Aqui, estado é a informação de trabalho desta execução.

```text
local informado nesta conversa
```

Contexto, estado e memória serão investigados com mais precisão no Encontro 05.

---
<!-- _class: question -->

# Onde entra a LLM padrão?

---

## A LLM sob restrições

```bash
uv run python praticas/encontro-03/02_ciclo_controlado.py
```

Ela recebe:

```text
objetivo + observação + estado + ações conversacionais
```

e devolve uma decisão estruturada.

<!-- [ESSENCIAL] A experiência padrão usa a LLM. Use o modo offline apenas quando a credencial ou a conectividade não estiverem disponíveis. -->

---

## O controlador ainda verifica a saída

```text
ação pertence ao conjunto permitido?
mensagem é texto?
decisão declara parada?
a combinação ação / parada é coerente?
```

<div class="statement">O modelo propõe. A arquitetura aceita, recusa ou continua.</div>

---
<!-- _class: trap -->

## O que uma LLM não ganha automaticamente

<div class="cards">
<div class="card">acesso a e-mail</div>
<div class="card">acesso a banco de dados</div>
<div class="card">acesso a terminal</div>
<div class="card">acesso a equipamentos ou sistemas institucionais</div>
</div>

---

## Com `--offline`, a LLM é simulada

```text
if local ausente → perguntar local
if local presente → orientar e encerrar
```

Essa alternativa não transforma a lição em “`if` versus LLM”.

<div class="statement">A arquitetura continua visível porque o problema é organizar informações, limites e continuidade.</div>

---
<!-- _class: synthesis -->

## Reconstrua o percurso

```text
uma resposta
→ não deixa clara uma trajetória

objetivo + percepção + estado + decisão limitada
→ permite escolher o próximo passo

controlador + validação + parada
→ produz um ciclo controlado
```

---
<!-- _class: synthesis -->

## Duas falhas, duas responsabilidades

<div class="columns">
<div class="card"><strong>Sem estado</strong><br>repete uma pergunta apesar de receber a resposta.</div>
<div class="card"><strong>Limite baixo</strong><br>encerra antes de usar a nova percepção.</div>
</div>

---
<!-- _class: takeaway -->

# Uma LLM pode participar da decisão.

# Um agente organiza decisões, informações, limites e consequências ao longo de uma trajetória.

---
<!-- _class: question -->

# O que ainda falta ao CampusBot?

```text
conversar ✓
manter estado ✓
controlar o ciclo ✓
agir no ambiente ?
```

---
<!-- _class: activity -->

## Missão autônoma — Localize a responsabilidade que falta

Abra:

```bash
uv run python praticas/encontro-03/atividade_autonoma.py
```

Antes de modificar código, registre:

```text
objetivo · percepção · estado · próximo passo · parada · limite atual
```

<!-- [ESSENCIAL] Oriente que é formativa, sem nota, e pode ser iniciada agora ou concluída durante a semana. -->

---

## Depois, compare as duas execuções

```bash
uv run python praticas/encontro-03/03_diagnosticar_o_ciclo.py --sem-estado
```

Registre:

1. a responsabilidade que falhou;
2. uma evidência no terminal;
3. a menor mudança arquitetural que a repararia.

---
<!-- _class: lead -->

# Que ferramenta ou capacidade externa o CampusBot precisaria ter

# para fazer mais do que responder?

<!-- [ESSENCIAL] Encerre com a tensão. Não antecipe a solução do Encontro 04. -->
