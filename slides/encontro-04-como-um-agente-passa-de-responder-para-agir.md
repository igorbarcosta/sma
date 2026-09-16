---
marp: true
theme: sma
paginate: true
title: Encontro 04 — Como um agente passa de responder para agir?
description: Sistemas Multiagentes / Agentic AI
---

<!-- _class: lead -->

# Como um agente passa de responder para agir?

Encontro 04 · Sistemas Multiagentes / Agentic AI

<!--
[ESSENCIAL]
Conduza como uma investigação única. Não apresente o diagrama final agora.
~0–10 min: resposta sem ação. ~10–35 min: ferramenta isolada e primeira conexão.
~35–75 min: tool loop. ~75–105 min: ambientes alternativos e resultado perdido.
~105–130 min: falha. ~130–150 min: síntese e início da missão autônoma.
-->

---

## O limite que ficou do Encontro 03

```text
CampusBot conversa ✓
CampusBot mantém um ciclo ✓
CampusBot consulta equipamentos ?
CampusBot abre chamados ?
```

<!-- [ESSENCIAL] Recupere apenas a tensão final do encontro anterior. -->

---
<!-- _class: question -->

# Uma resposta pode abrir um chamado?

---
<!-- _class: activity -->

## Execute antes de explicar

```bash
uv run python praticas/encontro-04/01_so_responde.py --offline
```

> “O projetor do Lab 4 não funciona. Abra um chamado.”

<!-- [ESSENCIAL] Peça uma previsão curta: “o que terá mudado depois?”. Execute cedo. -->

---

## O modelo pode dizer algo plausível

```text
“Eu abriria um chamado para o projetor do Lab 4.”
```

Mas o terminal também diz:

```text
Nenhum ambiente foi consultado ou modificado.
```

---
<!-- _class: question -->

# O que falta entre dizer e fazer?

<!-- [ESSENCIAL] Ouça hipóteses. Não apresente ferramenta, controlador ou loop ainda. -->

---
<!-- _class: takeaway -->

# Texto ≠ consequência no ambiente

---

## A menor mudança possível

```python
abrir_chamado(local, problema)
```

Primeiro: ela funciona sem LLM.

---
<!-- _class: activity -->

## Execute a ferramenta sozinha

```bash
uv run python praticas/encontro-04/02_primeira_ferramenta.py
```

Preveja o ambiente antes e depois.

<!-- [ESSENCIAL] Faça a turma encontrar a lista vazia e depois CH-001. -->

---

## O que a execução mostra

```text
ambiente antes:  []
                 ↓
abrir_chamado(...)
                 ↓
ambiente depois: [CH-001]
```

---
<!-- _class: question -->

# Quem abriu o chamado?

---

## Duas responsabilidades, por enquanto

<div class="columns">
<div class="card"><strong>Modelo</strong><br>escolhe ou solicita</div>
<div class="card"><strong>Ferramenta</strong><br>executa uma capacidade</div>
</div>

<div class="statement">Nesta execução não havia modelo. A ferramenta, chamada pelo programa, mudou o ambiente.</div>

---

## Vamos conectá-los sem esconder a fronteira

```text
modelo solicita uma ferramenta
          ↓
Python recebe nome + argumentos
          ↓
Python chama a função
```

<!-- [ESSENCIAL] Diga que não usaremos chamada automática: queremos ler cada responsabilidade. -->

---

## O contrato da decisão continua pequeno

```json
{"tipo": "usar_ferramenta",
 "ferramenta": "abrir_chamado",
 "argumentos": {"local": "Lab 4", "problema": "projetor não funciona"}}
```

ou

```json
{"tipo": "responder", "mensagem": "O chamado CH-001 foi aberto."}
```

---
<!-- _class: question -->

# E se antes precisamos descobrir
# se já há um chamado?

---

## O pedido muda

> “Veja se já existe um chamado. Se não existir, abra um.”

Agora existem duas ferramentas:

```python
consultar_chamados(local)
abrir_chamado(local, problema)
```

---
<!-- _class: activity -->

## Faça uma previsão da trajetória

```bash
uv run python praticas/encontro-04/03_agente_com_ferramentas.py --offline
```

> Qual ferramenta vem primeiro? O que a próxima decisão fará se a consulta estiver vazia?

<!-- [ESSENCIAL] Um minuto de previsão individual. Só depois execute e leia por blocos. -->

---

## Passo 1: o modelo solicita

```text
[MODELO]
Quero usar: consultar_chamados
Argumentos: {local: Lab 4}
```

---

## Passo 1: o programa executa

```text
[CONTROLADOR] Executando ferramenta...
[FERRAMENTA] consultar_chamados(...)
[RESULTADO] {ok: true, chamados: []}
```

---

## Passo 2: uma nova decisão

```text
[MODELO]
Quero usar: abrir_chamado
```

<div class="statement">A segunda decisão usa uma informação que não existia antes da primeira ferramenta.</div>

---

## Passo 2: o ambiente muda

```text
antes:  []
depois: [CH-001]
```

```text
[RESULTADO] {ok: true, protocolo: CH-001}
```

---

## Passo 3: o modelo responde

```text
“O chamado CH-001 foi aberto.”
```

<!-- [ESSENCIAL] Só agora percorra a trajetória inteira com a turma. -->

---
<!-- _class: takeaway -->

## O ciclo que acabamos de observar

```text
decidir
→ agir
→ observar
→ decidir novamente
```

---
<!-- _class: question -->

# Quem escreveu antecipadamente
# “consultar → abrir → responder”?

---

## Uma resposta curta

```text
controlador: escreve o ciclo
modelo: escolhe o próximo passo
ferramenta: produz o resultado
```

Em um workflow, a sequência poderia estar escrita de antemão. Aqui, ela é escolhida durante a execução a partir da observação.

---
<!-- _class: activity -->

## Mude o ambiente

```bash
uv run python praticas/encontro-04/03_agente_com_ferramentas.py \
  --com-chamado-existente --offline
```

Preveja: ele abrirá outro chamado?

<!-- [ESSENCIAL] A operação agora é comparar: mesma arquitetura, ambiente diferente. -->

---

## Com CH-001 já presente

```text
modelo → consultar_chamados
resultado → CH-001 existe
modelo → responder
```

<div class="statement">A ferramenta disponível é a mesma. O que mudou foi a observação.</div>

---
<!-- _class: question -->

# E se a ferramenta executa,
# mas seu resultado não volta?

---
<!-- _class: activity -->

## Corte uma passagem de propósito

```bash
uv run python praticas/encontro-04/03_agente_com_ferramentas.py \
  --com-chamado-existente --resultado-nao-volta --offline
```

<!-- [ESSENCIAL] Peça diagnóstico: o que está no ambiente? O que o modelo recebeu? -->

---

## O sintoma

```text
consultar_chamados executou ✓
CH-001 existe no ambiente ✓
resultado chegou ao modelo ✗

modelo pede consultar_chamados novamente
```

---
<!-- _class: takeaway -->

# O resultado da ferramenta
# vira informação para a próxima decisão.

---
<!-- _class: question -->

# Pedir uma ação prova que ela deu certo?

---
<!-- _class: activity -->

## Faça a abertura falhar

```bash
uv run python praticas/encontro-04/04_quando_a_ferramenta_falha.py --offline
```

<!-- [ESSENCIAL] Antes de executar, pergunte se o CampusBot pode afirmar sucesso. -->

---

## A ferramenta devolve uma evidência diferente

```json
{"ok": false, "erro": "serviço indisponível"}
```

O modelo recebe essa evidência e responde que não conseguiu abrir o chamado.

---
<!-- _class: takeaway -->

# Pedir uma ação
# ≠ executar uma ação
# ≠ a ação ter sucesso

---

## Quatro responsabilidades que a experiência pediu

| Parte | Pergunta que responde |
| --- | --- |
| Modelo | Qual é o próximo passo? |
| Ferramenta | Que capacidade o programa pode executar? |
| Ambiente | O que foi consultado ou mudou? |
| Controlador | Quem liga decisão, execução e nova observação? |

---
<!-- _class: synthesis -->

## Leia a arquitetura no código

```text
modelo.py → decisão
controlador.py → execução + ciclo
ferramentas.py → capacidade
ambiente.py → chamados em memória
```

<!-- [ESSENCIAL] Abra os arquivos. Mostre que os nomes não escondem as responsabilidades. -->

---
<!-- _class: takeaway -->

# A LLM escolhe.
# O programa executa.
# A ferramenta produz uma consequência no ambiente.
# O resultado volta para a próxima decisão.

---
<!-- _class: activity -->

## Missão autônoma — uma ferramenta a mais

```python
consultar_status(protocolo)
```

Produza uma execução com:

```text
decisão → solicitação → execução → resultado → decisão seguinte
```

<!-- [ESSENCIAL] É formativa e sem nota. Peça as cinco evidências da página, não somente código funcional. -->

---
<!-- _class: lead -->

# Quando uma LLM pede uma ferramenta,
# quem realmente a executa?

<!-- [ESSENCIAL] Encerrar pedindo uma resposta apontando modelo, controlador, ferramenta e ambiente no código. Não introduzir MCP, frameworks ou segurança de produção. -->
