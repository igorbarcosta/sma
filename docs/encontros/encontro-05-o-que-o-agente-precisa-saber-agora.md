# Encontro 05 — O que o agente precisa saber agora — e o que precisa lembrar depois?

**Pergunta orientadora:** **O que o agente precisa saber agora — e o que precisa lembrar depois?**

!!! tip "Abra o Codespace e atualize os materiais"

    Recomendamos continuar no Codespace da disciplina. Se ainda não tiver um, [abra o repositório no GitHub Codespaces](https://github.com/codespaces). No terminal, a partir da raiz do repositório, execute:

    ```bash
    git pull --ff-only
    uv sync --locked
    uv run python scripts/check_env.py
    ```

    Se o Git indicar que alterações suas impedem a atualização, preserve seu trabalho e consulte o [guia de ambiente](../materiais/ambiente.md). O mesmo projeto também pode ser executado localmente.

No [Encontro 04](encontro-04-como-um-agente-passa-de-responder-para-agir.md), o CampusBot aprendeu a consultar chamados e a abrir um novo. O modelo solicitava uma ferramenta, o programa a executava e devolvia o resultado para outra decisão. A última peça parecia estar no lugar: o agente já conseguia agir.

Mas imagine o pedido seguinte: “Veja se já existe um chamado para o projetor do Lab 4. Se não existir, abra um.” Se a consulta não encontrar nada, a próxima decisão parece simples. Será que basta a ferramenta devolver `[]` para o CampusBot avançar? Vamos seguir o resultado de uma rodada até a seguinte. Depois investigaremos o que acontece quando o decisor recebe informação demais, informação de menos ou uma informação que já não descreve o ambiente. Por fim, encerraremos o programa e perguntaremos o que ainda pode ser lembrado.

Os chamados são locais e fictícios. O modo `--offline` anuncia um decisor simulado e reproduzível. Sem ele, os ciclos principais usam Gemini configurado em `config/llm.toml` e exigem `GEMINI_API_KEY`. Nenhuma credencial é gravada.

Cada comando inicia uma versão isolada desse mesmo caso sintético; um chamado criado em um comando não aparece automaticamente no seguinte. A exceção será a experiência em que gravaremos deliberadamente um arquivo para outra execução. Antes de rodar cada versão, preveja sua próxima decisão. No terminal, as seções `[ESTADO ANTES]`, `[CONTEXTO ENVIADO AO MODELO]`, `[FICOU FORA]`, `[DECISÃO]` e `[RESULTADO DA FERRAMENTA]` permitem confrontar a previsão com o que ocorreu.

## O resultado chegou; por que o agente repete a consulta?

Lembre a cadeia que acabou de construir: `decidir → solicitar → executar → observar → decidir novamente`. Na primeira versão, a consulta devolve uma lista vazia. Antes de executar, responda: se nenhum chamado foi encontrado, qual deveria ser a próxima ferramenta?

```bash
uv run python praticas/encontro-05/01_esqueceu_o_resultado.py --offline
```

Procure primeiro `[RESULTADO DA FERRAMENTA]`: a consulta devolveu `{"ok": true, "chamados": []}`. Agora avance até `[ESTADO DEPOIS]`. `ultima_consulta` continua `null`. Na rodada seguinte, o contexto também não contém o resultado e a decisão solicita `consultar_chamados` outra vez. O limite de rodadas interrompe a repetição.

> A ferramenta falhou? O decisor recebeu uma consulta vazia e mesmo assim a ignorou? Ou a informação se perdeu entre uma rodada e outra?

As duas seções do terminal sustentam a terceira explicação: a consulta aconteceu, mas seu resultado foi descartado antes de poder orientar outra decisão. O aviso `[FALHA PLANEJADA]` torna essa passagem explícita. O problema não exige uma ferramenta nova; exige conservar uma descoberta da ferramenta que já existe.

Para testar a menor mudança, execute a versão que conserva o resultado da ferramenta. Ela chama `atualizar_estado(estado, ferramenta, resultado)` depois da execução:

```bash
uv run python praticas/encontro-05/02_estado_entre_passos.py --offline
```

Preveja novamente a sequência inteira. Desta vez, depois de `consultar_chamados`, `[ESTADO DEPOIS]` mostra `ultima_consulta` com a lista vazia. Na rodada seguinte, o mesmo resultado aparece em `[CONTEXTO ENVIADO AO MODELO]`. Só então o decisor solicita `abrir_chamado`; a ferramenta devolve `CH-001`, que também é conservado, e a última decisão responde com esse protocolo. Localize no terminal essas três decisões antes de seguir.

Agora a palavra **estado** serve para nomear algo observado: é a informação que o sistema mantém durante esta execução para que uma decisão posterior possa usar o que foi descoberto antes. `estado.py` expõe essa atualização em uma função pequena. O ambiente tem os chamados reais; o estado tem o que esta execução sabe deles. Eles podem divergir.

## O sistema sabe mais do que o decisor precisa agora

Guardar a consulta resolveu a repetição. Abra `estado.py` e observe que o sistema mantém também usuário, urgência, histórico, logs e preferência de idioma. Na próxima rodada, ele possui tudo isso, mas a decisão é apenas consultar ou abrir um chamado para o projetor. Que partes dessa informação você entregaria ao decisor?

Para observar o extremo de enviar tudo, faça esta comparação adicional. Você também pode seguir diretamente para a versão com informação de menos e voltar a esta depois:

```bash
uv run python praticas/encontro-05/03_contexto_demais.py --offline
```

Nessa versão, `[CONTEXTO ENVIADO AO MODELO]` reproduz o estado inteiro. A sequência ainda funciona no caso controlado. O terminal não demonstra que muita informação sempre provoca um erro. Ele mostra algo mais específico: `logs` e `preferencias` viajaram até o decisor sem ajudá-lo a escolher entre consultar, abrir ou responder. Ter informação disponível não obriga o sistema a enviá-la toda.

Podemos reduzir esse envio. Antes de executar a versão seguinte, faça uma aposta: basta passar `local` e `problema`?

```bash
uv run python praticas/encontro-05/04_contexto_de_menos.py --offline
```

Após a primeira consulta, `[ESTADO ANTES]` já contém `ultima_consulta` com `chamados: []`. Mas `[CONTEXTO ENVIADO AO MODELO]` contém apenas local e problema, e `[FICOU FORA]` lista `ultima_consulta`. O decisor repete a consulta. Agora o problema mudou de lugar: o sistema guardou o resultado, porém não o entregou nesta rodada. Compare essa falha com a primeira; as decisões se parecem, mas as evidências que explicam a repetição são diferentes.

Para separar o efeito da informação de outras possíveis causas, compare A e B:

```bash
uv run python praticas/encontro-05/05_comparacao_ab.py --offline
```

Os dois começam com o mesmo estado inicial, o mesmo objetivo, o mesmo prompt base, o mesmo decisor simulado e as mesmas ferramentas. A única diferença é o recorte produzido por `montar_contexto`: A não recebe o resultado da consulta; B recebe `chamados: []`. Antes de ler `[DECISÃO]`, preveja a escolha de cada um. A solicita `consultar_chamados`; B solicita `abrir_chamado`. A comparação usa o modo offline para isolar essa diferença; ao experimentar Gemini, as respostas podem variar.

Só agora vale nomear o segundo recorte:

```text
estado   = tudo que o sistema mantém nesta execução
contexto = informação entregue ao decisor nesta rodada
```

A conclusão nasce das duas decisões observadas: **a informação selecionada pelo sistema também determina o comportamento do agente**. Quando a decisão parece ruim, vale olhar o que chegou ao decisor antes de culpar o modelo.

Agora altere uma linha sua. Em `contexto.py`, faça o modo `de_menos` incluir o resultado da consulta. Rode `04_contexto_de_menos.py` novamente e compare a segunda decisão com a execução anterior. Seu registro deve mostrar qual campo entrou no contexto, qual ação mudou e por que essa mudança é suficiente. Se repetir o A/B depois da correção, A deverá passar a se comportar como B; isso também é evidência de que o recorte era a variável decisiva.

## A consulta guardada ainda descreve o ambiente?

O CampusBot já guarda a consulta e sabe entregá-la à decisão. Isso basta enquanto o ambiente permanece igual. Agora imagine que a consulta vazia foi feita antes de outra pessoa abrir `CH-001`. O estado ainda diz “nenhum chamado”, mas essa fotografia envelheceu. O que o CampusBot fará se usar essa informação sem verificar de novo?

```bash
uv run python praticas/encontro-05/06_informacao_desatualizada.py --offline
```

Na primeira trajetória, `[ESTADO ANTES]` traz a consulta vazia. A decisão pede `abrir_chamado`, e `[AMBIENTE]` passa a mostrar `CH-001` e `CH-002` no mesmo local. O resultado antigo foi preservado e entregue corretamente; faltou perguntar se ele ainda servia para esta decisão. A segunda trajetória começa novamente com o ambiente contendo apenas `CH-001`, descarta a consulta antiga e consulta de novo. Agora a resposta reconhece o chamado existente.

> Que evidência permite distinguir “o agente esqueceu” de “o agente lembrou uma informação antiga”?

Na primeira falha do encontro, `ultima_consulta` estava vazia. Aqui ela está preenchida, mas diverge do ambiente atual. Para este caso, uma nova consulta antes de abrir evita a duplicação. Não precisamos formular uma regra geral de validade para toda informação.

Há outra forma de a informação disponível induzir uma decisão ruim: duas indicações do mesmo dado discordam. O estado diz `Lab 4`, mas a pessoa corrige: “Na verdade, é no Lab 5.” Lá já existe `CH-001`. Antes de executar, preveja o que acontecerá se o programa continuar usando o local antigo.

```bash
uv run python praticas/encontro-05/07_informacao_conflitante.py --offline
```

O script mostra a nova percepção nas duas trajetórias. Na primeira, `estado.local` continua `Lab 4`: o CampusBot consulta esse local e abre um chamado ali. Na segunda, o programa atualiza `estado.local` para `Lab 5` antes de montar o contexto. A consulta encontra `CH-001`, e o agente responde sem abrir outro. Compare `[NOVA PERCEPÇÃO]`, `[ESTADO ANTES]` e `[CONTEXTO ENVIADO AO MODELO]` para localizar o momento da escolha. A experiência não resolve conflitos em geral; ela mostra uma escolha concreta de engenharia sobre qual informação orientar a decisão.

Uma variação do mesmo caso é retirar `ultima_abertura` do recorte em `contexto.py` e rodar `02_estado_entre_passos.py`. Preveja a decisão posterior à abertura, observe-a e restaure o campo depois. A ferramenta abriu o chamado; descubra por que a resposta final não acompanha essa mudança.

## O programa terminou. Qual era o protocolo?

Depois de abrir `CH-001`, encerre o programa. Abra uma nova execução e pergunte: “Qual era o protocolo do projetor do Lab 4?” `ultima_abertura` pertencia ao estado da execução anterior; um novo processo Python começa com outro estado. Antes de rodar os comandos, preveja o que a nova execução responderá sem ler nada que tenha sido gravado.

Use o mesmo caminho de arquivo nos dois comandos abaixo. Eles iniciam **processos diferentes**:

```bash
uv run python praticas/encontro-05/08_memoria_entre_execucoes.py --fase gravar --arquivo /tmp/campusbot-encontro-05.json --offline
uv run python praticas/encontro-05/08_memoria_entre_execucoes.py --fase recuperar --arquivo /tmp/campusbot-encontro-05.json --offline
```

O primeiro processo abre o chamado e grava um pequeno JSON. O segundo mostra `[NOVA EXECUÇÃO — ESTADO INICIAL]`: ali não há protocolo. Por isso, `[SEM MEMÓRIA]` responde que não sabe. Depois de `recuperar_memoria`, `[MEMÓRIA RECUPERADA]` mostra `CH-001`, e `[COM MEMÓRIA]` pode citar o protocolo. A diferença entre as duas respostas tem uma origem verificável: o arquivo foi lido entre elas. Se executar a fase `recuperar` antes de gravar o arquivo, a resposta continuará desconhecida.

Agora a palavra **memória** tem uma necessidade concreta: alguma informação precisa sobreviver além da execução que a descobriu. Aqui ela é apenas um arquivo JSON lido e gravado por `memoria.py`. A persistência resolve a pergunta pelo protocolo, mas cria uma nova dúvida: o arquivo sabe se o chamado continua aberto?

Imagine que o JSON diga `CH-001: aberto` e que, desde então, o chamado tenha sido encerrado. Preveja as duas respostas que o próximo comando mostrará: a primeira baseada na lembrança, a segunda depois de consultar o ambiente atual.

```bash
uv run python praticas/encontro-05/09_memoria_desatualizada.py --offline
```

Compare `[MEMÓRIA]` com `[AMBIENTE ATUAL]`. A primeira resposta repete “aberto”; a segunda diz “encerrado” depois da consulta. O protocolo lembrado ainda identifica o chamado, mas seu status antigo já não descreve o presente. Esquecer pode atrapalhar; lembrar um dado velho também.

Faça você uma intervenção pequena. No caso `memoria` de `atividade_autonoma.py`, a resposta inicial usa apenas a lembrança. Acrescente uma consulta ao ambiente antes de afirmar o status e mostre a resposta corrigida. Seu objetivo é resolver **este** desacordo observável, sem criar uma política geral de atualização.

### Para aprofundar a mesma investigação

Se ainda não executou a versão que envia o estado inteiro, faça isso agora e identifique quais campos não participaram da decisão. Depois compare com a variação que retira `ultima_abertura`: nesse caso, uma informação necessária ficou fora. As duas modificações aprofundam a mesma pergunta sobre a seleção do que chega ao decisor.

## Trabalho autônomo orientado

Rode os três casos de `atividade_autonoma.py`:

```bash
uv run python praticas/encontro-05/atividade_autonoma.py estado --offline
uv run python praticas/encontro-05/atividade_autonoma.py contexto --offline
uv run python praticas/encontro-05/atividade_autonoma.py memoria --offline
```

Em cada caso, identifique se o defeito principal está no estado, no contexto ou na memória. Cite uma linha da execução que sustente o diagnóstico, faça a menor correção, execute outra vez e explique a mudança de comportamento. Se já corrigiu o recorte em `contexto.py`, use a saída anterior e a posterior à sua intervenção como as duas evidências do caso `contexto`; não é preciso recriar o defeito. O arquivo `praticas/encontro-05/README.md` indica os arquivos de cada responsabilidade. A atividade é formativa e sem nota por padrão; sua produção será útil para a retomada do próximo encontro.

## Síntese e próximo problema

```text
ESTADO   O que o sistema mantém durante esta execução?
CONTEXTO O que o decisor recebe agora?
MEMÓRIA  O que pode sobreviver para outra execução?
```

A qualidade da decisão depende também da qualidade da informação disponível. Quando o CampusBot decide mal, como descobrir se a causa foi modelo, ferramenta, estado, contexto ou memória? Essa será a investigação do Encontro 06.
