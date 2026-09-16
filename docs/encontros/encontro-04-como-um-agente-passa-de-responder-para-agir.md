# Encontro 04 — Como um agente passa de responder para agir?

**Slides:** [Apresentação HTML](../slides/rendered/encontro-04-como-um-agente-passa-de-responder-para-agir.html) · [PDF](../slides/rendered/encontro-04-como-um-agente-passa-de-responder-para-agir.pdf)

**Pergunta orientadora**

> **Como um agente passa de responder para agir?**

No encontro anterior, o CampusBot conseguia conversar, conservar informações e escolher o próximo passo. Ele ainda não podia consultar equipamentos nem abrir chamados. Este encontro começa nesse limite. Vamos manter o mesmo problema durante toda a investigação e acrescentar apenas o que cada execução tornar necessário.

Todo chamado desta prática é local, sintético e fica apenas na memória durante a execução. Não há sistema institucional, dados reais, rede ou autenticação envolvidos.

!!! tip "Continue no mesmo ambiente"

    Da raiz do repositório, atualize o ambiente se necessário e comece pela primeira execução:

    ```bash
    uv sync --locked
    uv run python praticas/encontro-04/01_so_responde.py --offline
    ```

    O `--offline` anuncia uma simulação de decisão ou resposta. Sem essa opção, os programas que usam modelo solicitam Gemini conforme `config/llm.toml` e a sua `GEMINI_API_KEY`. A prática nunca grava ou mostra a chave.

## Ato 1 — Responder não é agir

Uma pessoa escreve para o CampusBot:

> “O projetor do Lab 4 não funciona. Abra um chamado.”

Execute a primeira versão:

```bash
uv run python praticas/encontro-04/01_so_responde.py --offline
```

Ela produz um texto plausível: talvez diga que abriria o chamado. Mas a última linha da execução importa mais que a frase:

```text
[OBSERVAÇÃO]
Nenhum ambiente foi consultado ou modificado.
```

Antes de continuar, responda: se o texto parece útil, o que ainda falta entre dizer e fazer?

Uma resposta é linguagem. Um chamado aberto seria uma mudança em outro sistema. Nesta primeira versão não existe sequer um ambiente para mudar. Portanto:

> **texto ≠ consequência no ambiente.**

Não é um problema de “boa” ou “má” LLM. Mesmo uma resposta muito convincente não prova que algo externo ocorreu.

## Ato 2 — Uma ferramenta faz algo que o modelo não faz

Antes de envolver o modelo, vamos isolar a menor capacidade que falta: `abrir_chamado(local, problema)`. Ela é uma função Python comum. Rode-a sozinha:

```bash
uv run python praticas/encontro-04/02_primeira_ferramenta.py
```

Compare as duas fotografias do ambiente que o terminal mostra. Antes, a lista de chamados está vazia. Depois, ela contém `CH-001`.

```text
[FERRAMENTA]
abrir_chamado(...)
        ↓
[AMBIENTE DEPOIS]
[{"protocolo": "CH-001", ...}]
```

> Quem abriu o chamado?

Não foi uma LLM: nesta execução nem há modelo. A **ferramenta** pediu uma alteração ao **ambiente**, e o programa Python a executou. Isso nos permite separar duas responsabilidades simples:

```text
modelo      escolhe ou solicita
ferramenta  executa uma capacidade
```

Agora podemos conectar uma decisão à ferramenta, sem esconder a fronteira em uma chamada automática do SDK. Abra os quatro arquivos centrais antes de rodar a versão seguinte:

```text
praticas/encontro-04/
├── ambiente.py      # sistema de chamados local e em memória
├── ferramentas.py   # consultar_chamados e abrir_chamado
├── modelo.py        # escolhe responder ou solicitar uma ferramenta
└── controlador.py   # executa a solicitação e devolve o resultado
```

Em particular, leia `executar_ciclo` em `controlador.py`. Seu fluxo principal é intencionalmente quase uma frase em português:

```text
decida

se decidiu responder:
    encerre

se decidiu usar ferramenta:
    execute
    observe o resultado
    volte a decidir
```

O contrato que chega do modelo tem só duas famílias. A primeira pede uma capacidade concreta:

```json
{
  "tipo": "usar_ferramenta",
  "ferramenta": "consultar_chamados",
  "argumentos": {"local": "Lab 4"}
}
```

A outra encerra a trajetória com uma resposta:

```json
{
  "tipo": "responder",
  "mensagem": "Já existe o chamado CH-001."
}
```

O nome e os argumentos não executam nada sozinhos. O controlador recebe essa estrutura e faz a chamada Python correspondente. Esse é o *manual tool handling* da prática: a decisão fica visível; a execução também.

## Ato 3 — A segunda decisão depende do que aconteceu

O pedido agora ficou um pouco mais interessante:

> “O projetor do Lab 4 não funciona. Veja se já existe um chamado. Se não existir, abra um.”

Antes de executar, preveja: qual ferramenta deve vir primeiro? E, se a consulta devolver uma lista vazia, qual deve ser a segunda?

```bash
uv run python praticas/encontro-04/03_agente_com_ferramentas.py --offline
```

Observe a trajetória, não apenas a frase final:

```text
modelo → consultar_chamados
resultado → nenhum chamado
modelo → abrir_chamado
resultado → CH-001
modelo → responder
```

Em cada passagem, o terminal separa a proposta, a execução, a mudança do ambiente e o resultado devolvido. Veja especialmente estas fronteiras:

```text
[MODELO]                 Quero usar: abrir_chamado
[CONTROLADOR]            Executando ferramenta...
[FERRAMENTA]             abrir_chamado(...)
[AMBIENTE DEPOIS]        agora contém CH-001
[RESULTADO DA FERRAMENTA] {"ok": true, "protocolo": "CH-001"}
```

> Quem escreveu antecipadamente a sequência “consultar → abrir → responder”?

O controlador escreveu o ciclo, mas não essa sequência específica. Ele sabe executar uma ferramenta solicitada e devolver seu resultado. O modelo escolhe o próximo passo a partir do pedido e dos resultados que já observou. Em um workflow, poderíamos ter programado explicitamente a ordem `consultar; se vazio, abrir; responder`. Aqui, a trajetória aparece em tempo de execução como uma sequência de decisões limitadas.

Só agora vale dar um nome curto ao que vimos. É o ciclo introduzido no Encontro 01, agora com uma consequência concreta:

```text
decidir
→ agir
→ observar
→ decidir novamente
```

Ou, com as responsabilidades que acabamos de executar:

```text
LLM propõe uma ação
→ programa recebe a decisão
→ ferramenta é executada
→ ambiente é consultado ou modificado
→ resultado volta ao modelo
→ nova decisão
```

### Mude o ambiente, não a arquitetura

Agora pré-carregue `CH-001` antes da execução:

```bash
uv run python praticas/encontro-04/03_agente_com_ferramentas.py --com-chamado-existente --offline
```

O modelo consulta, observa o protocolo existente e responde. Não abre outro chamado. A ferramenta disponível é a mesma; o ambiente observado mudou a decisão seguinte.

## Ato 4 — Pedir não é executar; executar não é conseguir

Até aqui, a abertura sempre funcionou. Vamos tornar o serviço indisponível de propósito:

```bash
uv run python praticas/encontro-04/04_quando_a_ferramenta_falha.py --offline
```

A primeira decisão continua pedindo `abrir_chamado`. O controlador ainda chama a ferramenta. Mas ela devolve:

```json
{"ok": false, "erro": "serviço indisponível"}
```

Observe a resposta seguinte. Ela reconhece que não conseguiu abrir o chamado.

> O agente poderia dizer que o chamado foi aberto?

Não. O pedido do modelo não é execução, e a execução não garante sucesso. O único fato que sustenta a resposta final é o resultado observado da ferramenta:

```text
pedir uma ação
≠ executar uma ação
≠ a ação ter sucesso
```

Essa diferença será útil quando estudarmos diagnóstico, validação, tentativas, segurança e avaliação. Por enquanto, fique com a pergunta mais concreta: **qual resultado a ferramenta realmente devolveu?**

## Experimento — e se o resultado não voltar?

No próximo comando, há um chamado existente. A consulta é executada corretamente, mas o controlador deliberadamente não entrega sua saída para a próxima decisão:

```bash
uv run python praticas/encontro-04/03_agente_com_ferramentas.py --com-chamado-existente --resultado-nao-volta --offline
```

O ambiente continua contendo `CH-001`; você o vê no terminal. Porém, o modelo não recebe o resultado e solicita `consultar_chamados` de novo até o limite de segurança.

Não diga apenas “o agente esqueceu”. Localize a passagem que foi cortada: **ferramenta executou → resultado não chegou ao modelo**. Isso explica por que uma consequência precisa voltar como informação para a decisão seguinte.

## A formulação que a execução construiu

Agora podemos nomear as quatro abstrações sem precisar decorar uma lista:

| Parte | O que faz neste CampusBot | O que não faz |
| --- | --- | --- |
| Modelo | Decide responder ou solicitar uma ferramenta. | Não chama a função Python nem altera a lista de chamados. |
| Ferramenta | Representa `consultar_chamados` ou `abrir_chamado`. | Não escolhe a trajetória seguinte. |
| Ambiente | Guarda os chamados locais em memória e sofre a mudança. | Não decide o que deve acontecer. |
| Controlador | Recebe a decisão, chama a ferramenta, entrega o resultado e mantém o ciclo. | Não inventa uma resposta de sucesso. |

> **A LLM escolhe. O programa executa. A ferramenta produz uma consequência no ambiente. O resultado volta para a próxima decisão.**

Há um limite externo de passos no controlador. Ele só impede um ciclo infinito nesta demonstração; não é uma nova categoria de decisão nem substitui a evidência produzida pela ferramenta.

## Missão autônoma — Acrescente uma capacidade pequena

Esta atividade é formativa e **sem nota**. Você pode iniciá-la no laboratório ou concluí-la durante a semana. Não precisa criar fork, branch, commit ou push.

Abra `praticas/encontro-04/atividade_autonoma.py`. A missão é acrescentar uma única ferramenta ao mesmo CampusBot:

```python
consultar_status(protocolo)
```

Use o chamado `CH-001` já preparado no ambiente. A nova ferramenta pode devolver um status simples, como `aberto`. Mantenha as responsabilidades visíveis: uma pequena função no ambiente, uma ferramenta, uma opção explícita no modelo e um ramo explícito de execução no controlador. Não crie registry, classes ou outro sistema.

Execute uma trajetória em que seja possível identificar:

```text
decisão
→ solicitação da ferramenta
→ execução pelo programa
→ resultado observado
→ decisão seguinte
```

Sua evidência de aprendizagem não é apenas “meu código funciona”. Registre estas cinco respostas:

1. Qual ferramenta foi solicitada?
2. Quem a executou de fato?
3. O que aconteceu no ambiente?
4. Qual resultado chegou ao modelo?
5. Como esse resultado influenciou o próximo passo?

## Síntese

O CampusBot não ganhou acesso mágico ao mundo quando usamos uma LLM. Ele ganhou uma capacidade porque o programa passou a oferecer uma ferramenta e a conectar a decisão a uma execução observável.

```text
responder
→ não prova uma consequência

solicitar uma ferramenta
→ programa a executa
→ ambiente muda ou é consultado
→ resultado informa a próxima escolha
```

Ainda não estudamos memória, RAG, MCP, frameworks, APIs reais, autenticação, retries sofisticados ou segurança de produção. Essas ideias podem importar mais tarde, mas não são necessárias para responder à pergunta deste encontro.

Antes de seguir, confirme que consegue apontar no código: onde está o ambiente, quem executa a ferramenta, onde o resultado volta ao modelo e por que uma frase que diz “abri o chamado” não é evidência suficiente.
