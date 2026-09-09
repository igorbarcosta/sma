# Encontro 02 — Quando vale a pena tornar um sistema agentivo?

**Pergunta orientadora**

> **Quando vale a pena tornar um sistema agentivo?**

No encontro anterior, localizamos ambiente, percepção, objetivo, decisão, ação e autonomia em arquiteturas diferentes. A pergunta que ficou foi mais incômoda: **mesmo que um sistema seja agente, ele precisava ser?**

Hoje não vamos responder por definição. Vamos construir sucessivas versões do **CampusBot**, uma central fictícia de solicitações de um campus. A cada novo requisito, você deverá prever o comportamento, executar, observar, modificar e decidir se vale comprar mais autonomia.

Todo dado desta prática é sintético. Não use dados reais de estudantes ou da instituição.

!!! tip "Abrir a prática no GitHub Codespaces"

    [Abrir no GitHub Codespaces](https://codespaces.new/igorbarcosta/sma/tree/main){ .md-button .md-button--primary }

    Aguarde a preparação automática. Quando o terminal estiver pronto, comece por:

    ```bash
    uv run python praticas/encontro-02/01_regras.py
    ```

    Prefere executar localmente? Use o [ambiente da disciplina](../materiais/ambiente.md).

## Antes de começar

Prepare o ambiente conforme o [guia de desenvolvimento](../materiais/ambiente.md). Da raiz do repositório, confira os arquivos:

```text
praticas/encontro-02/
├── README.md
├── casos.json
├── suporte.py
├── llm.py
├── 01_regras.py
├── 02_workflow_com_llm.py
├── 03_workflow_crescendo.py
├── 04_decisao_dinamica.py
├── mate_o_agente.py
└── atividade_autonoma.py
```

Nas etapas com LLM, o percurso usa por padrão o modelo definido em `config/llm.toml`. Para isso, configure uma `GEMINI_API_KEY` pessoal conforme o [guia de ambiente](../materiais/ambiente.md). O terminal anuncia um dos modos:

```text
MODO ONLINE — GEMINI
```

ou:

```text
MODO OFFLINE — RESPOSTA SIMULADA
```

Uma resposta preparada nunca será apresentada como saída do modelo. Se precisar executar sem chave ou sem internet, acrescente `--offline` ao comando para selecionar a simulação transparente.

## Missão 0 — O sistema precisava ser agente?

Recupere dois ou três sistemas analisados no trabalho autônomo anterior. Para cada um, troque a pergunta “é agente?” por esta:

> Qual seria a solução mais simples que talvez resolvesse esse problema?

Não precisamos encerrar o debate. Precisamos apenas de hipóteses para testar. O CampusBot nos permitirá resolver problemas semelhantes com quantidades diferentes de autonomia e observar o que cada escolha acrescenta.

## Missão 1 — O caso fácil

O CampusBot começa com uma situação confortável: a entrada já está estruturada.

```python
caso = {
    "categoria": "internet",
    "urgente": True,
    "local": "Lab 4",
}
```

Abra `praticas/encontro-02/01_regras.py`, mas não execute ainda. Leia a condição e **preveja a saída exata**. Depois rode:

```bash
uv run python praticas/encontro-02/01_regras.py
```

Compare a previsão com a saída. Em seguida, mude `urgente` para `False`, faça uma nova previsão e execute outra vez.

> O que uma LLM melhoraria neste caso?

??? "Análise depois da experiência"

    A entrada já separa categoria, urgência e local. A regra é conhecida, pequena e produz comportamento estável. Uma LLM não descobre informação ausente nem resolve uma ambiguidade relevante. Ela acrescentaria uma chamada, outra possibilidade de falha e maior variabilidade sem benefício claro para esse requisito.

    Isso não prova que regras sempre vencem. Prova apenas que, **neste problema**, a solução simples já é suficiente. Complexidade também é custo.

O código simples venceu. Mas o primeiro usuário real do CampusBot não respeita nosso formulário.

## Missão 2 — O usuário destrói nosso formulário

Agora chega apenas esta mensagem:

> “O Wi-Fi morreu no laboratório e minha apresentação começa daqui a pouco.”

O código anterior esperava `categoria`, `urgente` e `local`. Essas informações estão presentes, mas misturadas em linguagem natural. Abra `praticas/encontro-02/02_workflow_com_llm.py` e localize duas responsabilidades diferentes:

```text
linguagem natural
→ LLM extrai uma estrutura
→ regra escolhe a ação
→ código executa a consequência simulada
```

Antes de executar, preveja a estrutura extraída e a ação final. Então rode:

```bash
uv run python praticas/encontro-02/02_workflow_com_llm.py
```

Experimente também mensagens preparadas:

```bash
uv run python praticas/encontro-02/02_workflow_com_llm.py "A sala virou a Sibéria."
uv run python praticas/encontro-02/02_workflow_com_llm.py "Meu computador decidiu tirar férias."
```

Observe no terminal três fronteiras: o modo da LLM, a estrutura devolvida e a regra que escolheu a ação. O structured output limita a resposta a um objeto com categoria, urgência e local; o programa ainda valida esses campos antes de usá-los.

> Agora temos um agente?

??? "Análise depois da execução"

    A LLM resolveu uma incerteza de **interpretação**: transformou linguagem variada em uma estrutura pequena. Ela não escolheu quando pedir mais informação, abrir chamado ou encerrar. Essa trajetória continua sob controle explícito do workflow.

    Usar uma LLM e delegar o controle da trajetória são decisões diferentes. **Podemos usar uma LLM sem entregar a ela o controle da trajetória.**

### Alternativa offline

Se estiver sem chave ou sem internet, use a resposta simulada de modo explícito:

```bash
uv run python praticas/encontro-02/02_workflow_com_llm.py --offline
```

No modo padrão, o programa lê provider e modelo de `config/llm.toml`, solicita uma resposta estruturada pelo SDK `google-genai` e valida a estrutura recebida. Com `--offline`, nenhuma chamada externa é feita, mesmo que exista uma chave no ambiente.

## Missão 3 — O workflow começa a crescer

Um novo requisito chega:

> Não apenas classifique. Tente encaminhar ou resolver a solicitação.

Agora o CampusBot pode pedir informação, abrir chamado normal ou prioritário, fornecer orientação conhecida, encaminhar a uma pessoa ou encerrar. Ainda começaremos com um workflow explícito.

Abra `praticas/encontro-02/03_workflow_crescendo.py`. Preveja o resultado do caso padrão e execute:

```bash
uv run python praticas/encontro-02/03_workflow_crescendo.py
```

Teste outros ramos:

```bash
uv run python praticas/encontro-02/03_workflow_crescendo.py internet-urgente
uv run python praticas/encontro-02/03_workflow_crescendo.py computador-ferias
uv run python praticas/encontro-02/03_workflow_crescendo.py ajuda-incerta
```

O fluxo cresceu porque o requisito cresceu. Isso não torna o workflow ruim: seus ramos continuam visíveis, testáveis e fáceis de explicar.

### Novo requisito: editar de verdade

A equipe do campus agora possui uma orientação conhecida para climatização:

> Para uma sala muito fria, oriente a verificar o painel local e, se o problema continuar, registrar um chamado.

Execute primeiro o caso atual:

```bash
uv run python praticas/encontro-02/03_workflow_crescendo.py sala-fria
```

Depois abra `ORIENTACOES_CONHECIDAS`, acrescente a chave `climatizacao` com essa orientação e execute novamente. Compare a ação e a explicação antes e depois da edição.

> O novo requisito exigiu decisão dinâmica ou apenas uma regra conhecida?

??? "Análise depois da modificação"

    A regra adicional continua simples de declarar e inspecionar. O workflow absorveu o requisito sem perder clareza. Contar `if`s não decide se precisamos de um agente.

    A tensão legítima aparece quando não conhecemos antecipadamente a sequência necessária, quando o estado observado deve mudar a capacidade usada ou quando antecipar todos os caminhos passa a custar mais que delegar uma escolha limitada em execução. Ainda precisamos experimentar essa mudança.

## Uma formalização que agora tem motivo

As três versões já permitem distinguir organizações úteis sem tratá-las como uma taxonomia absoluta.

### Código determinístico

É adequado quando entradas e regras são suficientemente conhecidas, o comportamento pode ser especificado e a previsibilidade importa. Foi o que ocorreu no primeiro caso.

### Workflow

É adequado quando existe uma sequência ou conjunto de ramos conhecido. Ele pode usar uma LLM em etapas específicas e ainda manter explícito o controle da trajetória. Foi o que ocorreu quando a LLM extraiu campos e a regra decidiu o próximo passo.

### Decisão mais agentiva

Começa a fazer sentido quando não sabemos antecipadamente qual sequência será necessária, o estado observado precisa influenciar a capacidade usada e existe ganho real em delegar parte da escolha do próximo passo.

> **Agenticidade é uma decisão sobre responsabilidade e controle, não uma medalha de sofisticação.**

## Missão 4 — Quem escolhe o próximo passo?

Abra `praticas/encontro-02/04_decisao_dinamica.py`. Agora o componente de decisão recebe:

```text
objetivo + estado atual + ações permitidas
```

e devolve uma escolha estruturada:

```json
{
  "acao": "abrir_chamado_prioritario",
  "motivo": "há impacto imediato e o local é conhecido"
}
```

Antes de executar, preveja a decisão para `internet-urgente`:

```bash
uv run python praticas/encontro-02/04_decisao_dinamica.py internet-urgente
```

Depois compare com um estado incompleto:

```bash
uv run python praticas/encontro-02/04_decisao_dinamica.py computador-ferias
```

No modo padrão, a escolha é delegada ao modelo. Com `--offline`, uma decisão simulada torna o percurso reproduzível sem chamada externa. Nos dois modos, Python valida a ação, limita as possibilidades e executa apenas uma consequência simulada. A LLM não executa código arbitrário e não há tool calling.

> **Ainda não construímos um agente completo.** Apenas deslocamos parte da decisão do próximo passo para tempo de execução, produzindo uma **decisão mais agentiva**. Ainda não há um ciclo contínuo de percepção, decisão, ação e nova percepção, nem execução autônoma de uma sequência adaptativa, tool calling ou um runtime agentivo completo. Esses elementos serão estudados em outros momentos.

```bash
uv run python praticas/encontro-02/04_decisao_dinamica.py internet-urgente --offline
```

Compare a distribuição de responsabilidades:

```text
workflow
programador define a trajetória

decisão mais agentiva
programador define objetivo, limites e possibilidades
sistema escolhe parte da trajetória em execução
```

> O que ganhamos? O que passamos a pagar?

??? "Pontos para conferir na observação"

    Ganhamos flexibilidade para escolher uma ação a partir do estado sem codificar antecipadamente o ramo exato. Em troca, reduzimos previsibilidade, acrescentamos uma chamada ao modelo, percebemos latência e tornamos algumas falhas mais difíceis de explicar.

    A validação e a lista de ações preservam limites importantes, mas não eliminam custo ou variabilidade. A pergunta não é se essa arquitetura é mais moderna; é se a flexibilidade comprada serve ao requisito.

## Arena de Arquiteturas

Chegou a hora de colocar lado a lado:

```text
A — regras
B — workflow + LLM
C — decisão dinâmica
```

Abra `praticas/encontro-02/casos.json`. Para cada caso escolhido, antes de executar, registre **qual é a menor arquitetura que você espera ser suficiente** e por quê. Depois distribua o caso entre os programas e use esta ficha de observação:

| Observação | A — regras | B — workflow + LLM | C — decisão dinâmica |
|---|---|---|---|
| Resolveu o requisito? | | | |
| Foi simples de entender? | | | |
| Exigiu LLM? | | | |
| Houve decisão dinâmica? | | | |
| Foi fácil explicar o comportamento? | | | |
| A complexidade acrescentada foi útil? | | | |

Você não precisa produzir um ranking. Um caso pode ser inadequado para determinada versão, e duas arquiteturas podem ser suficientes. A decisão arquitetural deve considerar o requisito, não uma competição abstrata entre tecnologias.

Escolha um identificador e passe o mesmo valor às quatro versões. Comece, por exemplo, com `internet-urgente`:

```bash
uv run python praticas/encontro-02/01_regras.py internet-urgente
uv run python praticas/encontro-02/02_workflow_com_llm.py internet-urgente
uv run python praticas/encontro-02/03_workflow_crescendo.py internet-urgente
uv run python praticas/encontro-02/04_decisao_dinamica.py internet-urgente
```

Depois repita a comparação com um requisito diferente:

```bash
uv run python praticas/encontro-02/01_regras.py mochila-perdida
uv run python praticas/encontro-02/02_workflow_com_llm.py mochila-perdida
uv run python praticas/encontro-02/03_workflow_crescendo.py mochila-perdida
uv run python praticas/encontro-02/04_decisao_dinamica.py mochila-perdida
```

> **Qual é a menor arquitetura suficiente para este problema?**

## Atividade central — Mate o agente

O arquivo `praticas/encontro-02/mate_o_agente.py` resolve um caso simples por decisão dinâmica:

```bash
uv run python praticas/encontro-02/mate_o_agente.py
```

Sua missão em dupla é direta:

> **O agente está demitido. Resolva o mesmo requisito com a arquitetura mais simples possível.**

Edite o arquivo para remover a chamada a `decidir`. Você pode usar uma regra, um workflow ou uma LLM somente para extração, se realmente precisar. Preserve o requisito e compare a consequência antes e depois. A solução deve continuar executável.

Quando a simplificação funcionar, acrescente este requisito:

> Se o local do objeto não for conhecido, peça essa informação antes de orientar.

Execute com `local = None` e pergunte:

> Sua simplificação continua suficiente?

??? "O que conta como sucesso?"

    Não existe obrigação de voltar para decisão via LLM. Se uma condição pequena continua clara e suficiente, mantê-la é uma boa decisão. Se novos requisitos produzirem uma escolha que realmente dependa de estado e possibilidades difíceis de antecipar, então poderemos reavaliar a distribuição do controle.

    **Engenharia agentiva também é saber remover autonomia.**

## Síntese — quanta autonomia vale comprar?

Reconstrua o caminho antes de abrir a síntese:

```text
dados estruturados
→ regra bastou

linguagem natural
→ LLM ajudou
→ workflow continuou suficiente

requisitos aumentaram
→ workflow cresceu sem se tornar automaticamente inadequado

decisão em execução
→ autonomia ofereceu flexibilidade
→ também trouxe novos custos
```

Não buscamos a arquitetura mais agentiva. Buscamos a menor autonomia que sustenta o requisito e seus trade-offs.

> **LLM e agente não são sinônimos.**

> **Workflow não é uma versão inferior de agente.**

> **Mais autonomia cria possibilidades e também custos.**

> **Use a menor autonomia suficiente para resolver o problema.**

## Missão autônoma — A menor arquitetura suficiente

Esta atividade é formativa e **sem nota**. Você pode iniciá-la no laboratório ou realizá-la em casa ao longo da semana, continuando no mesmo Codespace usado durante a aula. Não é necessário criar fork, branch, commit ou push. O resultado será retomado no Encontro 03.

Abra `praticas/encontro-02/atividade_autonoma.py` e crie **uma** nova solicitação sintética para o CampusBot. Preencha também o pequeno bloco `MINHA HIPÓTESE` no próprio arquivo: esse registro será retomado no início do Encontro 03. A solicitação pode ser realista ou divertida, por exemplo:

- “A máquina do laboratório não compila meu código e a prova começa em quinze minutos.”
- “Perdi um pendrive e não sei em qual laboratório.”
- “A sala está sem projetor, mas talvez exista outro disponível.”

Seu trabalho é:

1. adicionar o novo caso;
2. escolher regra, workflow, workflow + LLM ou decisão mais agentiva;
3. implementar ou adaptar a solução;
4. executar e observar o resultado;
5. registrar brevemente o que aconteceu;
6. justificar por que **não** escolheu uma arquitetura mais complexa.

O objetivo é transferir a decisão arquitetural para um caso criado por você. Uma solução simples que continua suficiente é um excelente resultado.

Termine seu registro com a pergunta que abrirá o próximo encontro:

> **Se você precisasse transformar essa solução em um agente mais completo, que componentes acha que seriam necessários?**
