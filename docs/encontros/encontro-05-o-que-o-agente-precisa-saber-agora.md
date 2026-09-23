# Encontro 05 — O que o agente precisa saber agora — e o que precisa lembrar depois?

**Pergunta orientadora:** **O que o agente precisa saber agora — e o que precisa lembrar depois?**

!!! tip "Abra o Codespace e atualize os materiais"

    Recomendamos continuar no Codespace da disciplina. Se ainda não tiver um, [abra o repositório no GitHub Codespaces](https://codespaces.new/igorbarcosta/sma/tree/main). No terminal, a partir da raiz do repositório, execute:

    ```bash
    git pull --ff-only
    uv sync --locked
    uv run python scripts/check_env.py
    ```

    Se o Git indicar que alterações suas impedem a atualização, preserve seu trabalho e consulte o [guia de ambiente](../materiais/ambiente.md). O mesmo projeto também pode ser executado localmente.

No [Encontro 04](encontro-04-como-um-agente-passa-de-responder-para-agir.md), o CampusBot aprendeu a solicitar `consultar_chamados` e `abrir_chamado`. O programa executava a ferramenta, devolvia o resultado e pedia uma nova decisão. Agora ele já consegue agir. Vamos investigar o que ocorre quando a informação que chega à próxima decisão é pouca, excessiva ou incorreta — e quando a execução termina.

**Slides de condução:** [HTML](../slides/rendered/encontro-05-o-que-o-agente-precisa-saber-agora.html) · [PDF](../slides/rendered/encontro-05-o-que-o-agente-precisa-saber-agora.pdf). A página e a prática em `praticas/encontro-05/` bastam para estudar sem eles.

Os chamados são locais e fictícios. O modo `--offline` anuncia um decisor simulado e reproduzível. Sem ele, os ciclos principais usam Gemini configurado em `config/llm.toml` e exigem `GEMINI_API_KEY`. Nenhuma credencial é gravada.

Em cada experimento, **preveja** a próxima decisão antes de executar. Depois leia `[ESTADO ANTES]`, `[CONTEXTO ENVIADO AO MODELO]`, `[FICOU FORA]`, `[DECISÃO]` e `[RESULTADO DA FERRAMENTA]`. Explique a saída antes de passar ao próximo. Os nove experimentos são variações do mesmo pedido: “Veja se já existe um chamado para o projetor do Lab 4. Se não existir, abra um.”

## Ato 1 — O resultado chegou; por que o agente repete a consulta? (aprox. 0–50 min)

Retome apenas a cadeia `decidir → solicitar → executar → observar → decidir`. Então rode, antes de definir qualquer conceito novo:

```bash
uv run python praticas/encontro-05/01_esqueceu_o_resultado.py --offline
```

**Experimento 1 — resultado descartado.** Preveja o que ocorre depois de `consultar_chamados("Lab 4")` devolver `[]`. A ferramenta funcionou, mas o controlador descarta o resultado de propósito. Na rodada seguinte, `ultima_consulta` ainda é `null`; a decisão solicita a mesma consulta. O limite de rodadas interrompe a repetição. A falha está no modelo, na ferramenta ou entre uma rodada e outra? A saída separa essas possibilidades.

Faça a menor mudança conceitual: conservar o resultado da ferramenta. A versão seguinte chama `atualizar_estado(estado, ferramenta, resultado)` depois da execução:

```bash
uv run python praticas/encontro-05/02_estado_entre_passos.py --offline
```

**Experimento 2 — resultado conservado.** Preveja a sequência de três decisões. Confira: consultar, abrir, responder. Compare o valor de `ultima_consulta` antes e depois da ferramenta e localize o instante em que a segunda decisão passa a poder usar a descoberta.

Agora a palavra **estado** serve para nomear algo observado: é a informação que o sistema mantém durante esta execução para que uma decisão posterior possa usar o que foi descoberto antes. `estado.py` expõe essa atualização em uma função pequena. O ambiente tem os chamados reais; o estado tem o que esta execução sabe deles. Eles podem divergir.

## Ato 2 — O sistema sabe mais do que o decisor precisa agora (aprox. 50–100 min)

Abra `estado.py`. Além da consulta, há usuário, urgência, histórico, logs e preferência de idioma. A pergunta é concreta: tudo isso precisa entrar em toda decisão?

```bash
uv run python praticas/encontro-05/03_contexto_demais.py --offline
uv run python praticas/encontro-05/04_contexto_de_menos.py --offline
```

**Experimento 3 — informação demais.** O recorte `demais` manda todo o estado. Compare o tamanho e a relevância dos campos com a decisão. Neste caso sintético, a ação ainda pode estar correta; a evidência é que logs e preferências foram enviados sem ajudar a decidir sobre a consulta. Não conclua que todo contexto grande necessariamente causa erro.

**Experimento 4 — informação de menos.** O sistema conserva a consulta, mas o recorte só entrega local e problema. Preveja a segunda decisão. Ela volta a consultar, embora `[ESTADO ANTES]` já contenha `ultima_consulta`. Localize a linha que mostra a exclusão.

**Experimento 5 — comparação A/B controlada.** Rode:

```bash
uv run python praticas/encontro-05/05_comparacao_ab.py --offline
```

O A e o B recebem o mesmo estado inicial, modelo, prompt base, ferramentas e objetivo. A única mudança é `montar_contexto`: A omite a consulta; B inclui a consulta vazia. A pede `consultar_chamados`; B pede `abrir_chamado`. Compare as seções `[CONTEXTO ENVIADO AO MODELO]` e `[DECISÃO]` antes de interpretar. Em modo online, a saída da LLM pode variar; o modo offline isola a variável do experimento.

Só agora vale nomear o segundo recorte:

```text
estado   = tudo que o sistema mantém nesta execução
contexto = informação entregue ao decisor nesta rodada
```

A conclusão nasce do A/B: **nem todo erro do agente é erro do modelo; a informação selecionada pelo sistema também muda sua decisão**. O terminal deixa visível o que ficou fora.

**Intervenção 1.** Em `contexto.py`, corrija o modo `de_menos` para incluir o resultado da consulta. Execute os experimentos 4 e 5 novamente. Mostre o campo incluído e a ação que mudou. Reponha o defeito original se quiser repetir a demonstração com outra pessoa.

## Ato 3 — Ter um dado não garante que ele esteja certo (aprox. 100–150 min)

**Experimento 6 — dado desatualizado.** Uma consulta antiga dizia “nenhum chamado”, mas o ambiente agora contém `CH-001`:

```bash
uv run python praticas/encontro-05/06_informacao_desatualizada.py --offline
```

Preveja a primeira decisão e compare estado com `[AMBIENTE]`. Ela abre `CH-002`: o estado conservou um resultado verdadeiro no passado, mas inadequado agora. Na segunda tentativa, o programa descarta a consulta antiga, consulta de novo e encontra `CH-001`. A correção específica aqui é verificar o ambiente antes de abrir; não precisamos de uma política geral de validade temporal.

**Experimento 7 — dado conflitante.** O estado diz `Lab 4`; uma nova percepção corrige para `Lab 5`, onde `CH-001` já existe:

```bash
uv run python praticas/encontro-05/07_informacao_conflitante.py --offline
```

Primeiro, a correção fica fora do estado e o CampusBot consulta e abre no Lab 4. Depois, o local do estado é atualizado para Lab 5 e o agente encontra o chamado existente. Qual linha mostra que a escolha foi feita antes da chamada ao modelo? A atividade não pretende resolver conflitos em geral; ela mostra que montar informação para a decisão é uma escolha de engenharia.

**Extensão pronta, se houver tempo:** em `estado.py`, acrescente uma segunda observação de local; execute com a antiga e a nova em ordens opostas. Explique qual valor `montar_contexto` entrega. Outra extensão é remover apenas `problema` do recorte e observar a validação da decisão; depois restaurá-lo. Essas variações aprofundam o mesmo problema, sem abrir tema novo.

## Ato 4 — A execução terminou. O que restou? (aprox. 150–200 min)

O estado anterior desaparece quando o processo Python acaba. Faça duas sessões separadas com um arquivo JSON escolhido por você:

```bash
uv run python praticas/encontro-05/08_memoria_entre_execucoes.py --fase gravar --arquivo /tmp/campusbot-encontro-05.json --offline
uv run python praticas/encontro-05/08_memoria_entre_execucoes.py --fase recuperar --arquivo /tmp/campusbot-encontro-05.json --offline
```

**Experimento 8 — duas execuções.** Antes de recuperar, a nova execução diz que não sabe o protocolo. Depois de `recuperar_memoria`, responde `CH-001`. Compare `[NOVA EXECUÇÃO — ESTADO INICIAL]` com `[MEMÓRIA RECUPERADA]`. O estado novo não herdou os objetos do processo anterior; o JSON sobreviveu. Se rodar `recuperar` antes de `gravar`, o arquivo pode não existir e a resposta continuará desconhecida.

Neste encontro, **memória** é simplesmente informação que pode sobreviver a uma execução. `memoria.py` contém `salvar_memoria` e `recuperar_memoria`. Persistir o protocolo não prova que seu status continuará atual.

```bash
uv run python praticas/encontro-05/09_memoria_desatualizada.py --offline
```

**Experimento 9 — lembrança antiga.** O JSON diz que `CH-001` está aberto. O ambiente atual diz que ele foi encerrado. A primeira resposta repete o status antigo. Depois, uma consulta atual corrige a informação usada na resposta. Preveja as duas respostas e aponte a linha que sustenta cada uma. **Intervenção 2:** em `atividade_autonoma.py`, caso `memoria`, implemente apenas a conferência no ambiente antes de afirmar o status. Mostre a resposta corrigida. Esquecer pode atrapalhar; lembrar dado velho também.

### Núcleo e extensões

O **núcleo** é a sequência 1, 2, 4, 5, 6, 7, 8 e 9, com as duas intervenções. O experimento 3 é uma extensão curta sobre excesso de informação; as variações de local e de campo removido são extensões para uma turma que avance rápido. A distribuição de tempos é uma referência para conduzir previsão, execução, conversa em pares e correção, não um cronograma rígido.

## Trabalho autônomo orientado

Rode os três casos de `atividade_autonoma.py`:

```bash
uv run python praticas/encontro-05/atividade_autonoma.py estado --offline
uv run python praticas/encontro-05/atividade_autonoma.py contexto --offline
uv run python praticas/encontro-05/atividade_autonoma.py memoria --offline
```

Em cada caso, identifique se o defeito principal está no estado, no contexto ou na memória; cite uma linha da execução; faça a menor correção; execute outra vez; explique por que o comportamento mudou. No caso `estado`, ative a preservação do resultado. No caso `contexto`, inclua a consulta já guardada no recorte. No caso `memoria`, confira o status no ambiente antes da resposta. O arquivo `praticas/encontro-05/README.md` indica os arquivos de cada responsabilidade. A atividade é formativa e sem nota por padrão; sua produção será útil para a retomada do próximo encontro.

## Síntese e próximo problema

```text
ESTADO   O que o sistema mantém durante esta execução?
CONTEXTO O que o decisor recebe agora?
MEMÓRIA  O que pode sobreviver para outra execução?
```

A qualidade da decisão depende também da qualidade da informação disponível. Quando o CampusBot decide mal, como descobrir se a causa foi modelo, ferramenta, estado, contexto ou memória? Essa será a investigação do Encontro 06.
