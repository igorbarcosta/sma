---
marp: true
theme: sma
paginate: true
title: Encontro 05 — O que o agente precisa saber agora?
description: Sistemas Multiagentes / Agentic AI
---

<!-- _class: lead -->

# O que o agente precisa saber agora — e o que precisa lembrar depois?

Encontro 05 · CampusBot

<!-- [NÚCLEO] ~0–5 min. Retome o ciclo do Encontro 04 em uma frase. Não defina estado, contexto ou memória. -->

---
<!-- _class: question -->

# O CampusBot já consegue agir.
# O que acontece se ele esquecer o resultado?

---
<!-- _class: activity -->

## Preveja a segunda decisão

> “Veja se há chamado para o projetor do Lab 4. Se não houver, abra um.”

```text
consultar_chamados("Lab 4") → []
próxima decisão → ?
```

<!-- [NÚCLEO] ~5–10 min. Peça previsão individual, sem apresentar o defeito. -->

---
<!-- _class: activity -->

## Execute a falha

```bash
uv run python praticas/encontro-05/01_esqueceu_o_resultado.py --offline
```

Encontre o resultado da ferramenta e o estado da rodada seguinte.

<!-- [NÚCLEO] ~10–20 min. Pergunte: falhou ferramenta, modelo ou passagem entre rodadas? -->

---
<!-- _class: trap -->

## O sintoma

```text
consulta → []
resultado descartado
nova decisão → consultar outra vez
```

Qual linha do terminal prova que a ferramenta funcionou?

---
<!-- _class: activity -->

## Faça a menor alteração

```python
atualizar_estado(estado, "consultar_chamados", resultado)
```

```bash
uv run python praticas/encontro-05/02_estado_entre_passos.py --offline
```

<!-- [NÚCLEO] ~20–40 min. Compare decisões e estado antes/depois. Deixe os alunos explicar antes da formalização. -->

---
<!-- _class: concept -->

## Agora podemos nomear

**Estado** é o que o sistema mantém nesta execução para usar em uma decisão posterior.

```text
consultar → guardar resultado → decidir de novo
```

<!-- [NÚCLEO] ~40–50 min. Formalização curta; abra estado.py. -->

---
<!-- _class: question -->

# Se o sistema guarda mais informação,
# tudo deve ir para o modelo?

<!-- [NÚCLEO] ~50 min. Mostre os campos de estado.py; peça seleção antes da execução. -->

---
<!-- _class: activity -->

## Informação demais

```bash
uv run python praticas/encontro-05/03_contexto_demais.py --offline
```

Quais campos ajudam a decidir se deve abrir um chamado?

<!-- [EXTENSÃO] ~8–12 min. A ação pode estar correta; o ponto é a irrelevância observável de logs e preferências. Use se houver tempo ou após o A/B. -->

---
<!-- _class: activity -->

## Informação de menos

```bash
uv run python praticas/encontro-05/04_contexto_de_menos.py --offline
```

O que o estado já sabe? O que foi enviado? O que ficou fora?

<!-- [NÚCLEO] ~60–75 min. Prever a segunda decisão; pedir que apontem as duas seções do terminal. -->

---
<!-- _class: question -->

# Dois agentes iguais podem decidir diferente
# apenas pelo que recebem agora?

---
<!-- _class: activity -->

## Experimento A/B

```bash
uv run python praticas/encontro-05/05_comparacao_ab.py --offline
```

```text
A → consulta ausente do recorte
B → consulta vazia presente no recorte
```

Mesmo modelo, prompt, ferramentas, objetivo e estado inicial.

<!-- [NÚCLEO] ~75–90 min. Antes de executar, recolha duas previsões. Compare apenas contexto e decisão; não atribua erro à LLM. -->

---
<!-- _class: concept -->

## A distinção que o A/B exigiu

```text
estado   → tudo que o sistema mantém nesta execução
contexto → recorte entregue ao decisor nesta rodada
```

<!-- [NÚCLEO] ~90–100 min. Abra contexto.py e faça a intervenção 1: incluir ultima_consulta no modo de_menos; executar outra vez. -->

---
<!-- _class: takeaway -->

# Uma decisão ruim pode vir
# da informação que o sistema entregou.

---
<!-- _class: question -->

# E se a informação recebida
# era verdadeira ontem?

---
<!-- _class: activity -->

## Consulta antiga, ambiente novo

```bash
uv run python praticas/encontro-05/06_informacao_desatualizada.py --offline
```

Preveja: com “nenhum chamado” no estado e `CH-001` no ambiente, o que acontece?

<!-- [NÚCLEO] ~100–125 min. Ler a duplicação CH-002 e a segunda tentativa com consulta nova. Peça evidência do desacordo. Não introduzir TTL. -->

---
<!-- _class: trap -->

## Ter uma informação não basta

```text
estado: nenhuma ocorrência encontrada antes
ambiente agora: CH-001 aberto
```

Qual informação serve para esta decisão?

---
<!-- _class: activity -->

## Duas indicações de local

```text
estado.local = Lab 4
nova percepção = “Na verdade, Lab 5.”
```

```bash
uv run python praticas/encontro-05/07_informacao_conflitante.py --offline
```

<!-- [NÚCLEO] ~125–145 min. Prever as duas trajetórias. Pergunte quando a correção precisa entrar no estado/contexto. Não ensinar política geral de conflitos. -->

---
<!-- _class: synthesis -->

## O que vimos até aqui?

```text
faltou resultado → repete
recorte insuficiente → repete
consulta antiga → duplica
local antigo → age no lugar errado
```

<!-- [EXTENSÃO] ~145–150 min. Em pares, retire um campo do contexto ou altere a ordem de duas percepções; peça previsão e execução. -->

---
<!-- _class: question -->

# O programa terminou.
# Qual era o protocolo?

<!-- [NÚCLEO] ~150 min. Faça o professor encerrar o processo; abra novo terminal ou nova execução. Não diga memória ainda. -->

---
<!-- _class: activity -->

## Dois processos, um JSON local

```bash
uv run python praticas/encontro-05/08_memoria_entre_execucoes.py \
  --fase gravar --arquivo /tmp/campusbot-encontro-05.json --offline
```

Depois execute com `--fase recuperar` e o mesmo arquivo.

<!-- [NÚCLEO] ~150–175 min. Peça previsão da resposta antes e depois da leitura. Compare estado inicial novo e memória recuperada. -->

---
<!-- _class: concept -->

## O que sobreviveu?

```text
estado novo → não contém o protocolo
JSON local → contém CH-001
```

**Memória** é informação que pode sobreviver além da execução.

---
<!-- _class: question -->

# Lembrar sempre ajuda?

---
<!-- _class: activity -->

## O status lembrado está velho

```bash
uv run python praticas/encontro-05/09_memoria_desatualizada.py --offline
```

```text
memória: CH-001 aberto
ambiente: CH-001 encerrado
```

<!-- [NÚCLEO] ~175–190 min. Prever as duas respostas; iniciar intervenção 2 em atividade_autonoma.py. Não aprofundar atualização geral. -->

---
<!-- _class: synthesis -->

## Três perguntas para qualquer decisão

```text
ESTADO   O que o sistema mantém nesta execução?
CONTEXTO O que o decisor recebe agora?
MEMÓRIA  O que pode sobreviver a outra execução?
```

---
<!-- _class: activity -->

## Sua investigação continua

```bash
uv run python praticas/encontro-05/atividade_autonoma.py estado --offline
uv run python praticas/encontro-05/atividade_autonoma.py contexto --offline
uv run python praticas/encontro-05/atividade_autonoma.py memoria --offline
```

Para cada caso: evidência → menor correção → nova execução → explicação.

<!-- [NÚCLEO] ~190–200 min. Comece pelo primeiro caso; o trabalho é formativo. Extensão: comparar quais campos ficaram fora do contexto em cada execução. -->

---
<!-- _class: lead -->

# Se a decisão ficou ruim, como descobrir a causa?

Modelo · ferramenta · estado · contexto · memória

Encontro 06: observar e diagnosticar.

<!-- [NÚCLEO] Termine pedindo uma evidência concreta para uma das cinco causas, sem antecipar métodos do próximo encontro. -->
