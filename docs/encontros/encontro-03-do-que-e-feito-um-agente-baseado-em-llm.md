# Encontro 03 — Do que é feito um agente baseado em LLM?

**Pergunta orientadora**

> **Do que é feito um agente baseado em LLM?**

No encontro anterior, o CampusBot passou a escolher parte de sua trajetória em tempo de execução. Isso nos ajudou a localizar uma diferença importante entre um workflow e uma decisão mais agentiva. Mas a decisão apareceu quase como uma caixa: entravam objetivo, estado e ações permitidas; saía uma escolha.

Agora precisamos abrir essa caixa, sem confundir seus componentes. Uma LLM pode produzir uma boa resposta para uma pessoa e, ainda assim, não sustentar sozinha um agente. O que faz o sistema continuar, incorporar uma nova percepção, respeitar limites e saber a hora de parar?

Usaremos novamente um caso sintético do CampusBot. Nenhum exemplo usa dados reais de estudantes ou da instituição.

!!! tip "Continue no seu Codespace do Encontro 02"

    Abra o Codespace que você já criou para a disciplina. Da raiz do repositório, atualize os materiais e o ambiente:

    ```bash
    git pull --ff-only
    uv sync --locked
    ```

    Em seguida, comece por:

    ```bash
    uv run python praticas/encontro-03/01_uma_resposta.py
    ```

    Não crie outro Codespace apenas para este encontro. Se você ainda não tem um ambiente da disciplina, use o [guia de ambiente](../materiais/ambiente.md).

## Antes de começar

Da raiz do repositório, você encontrará esta prática:

```text
praticas/encontro-03/
├── README.md
├── casos.py
├── modelo.py
├── agente.py
├── 01_uma_resposta.py
├── 02_ciclo_controlado.py
├── 03_diagnosticar_o_ciclo.py
├── 04_validar_decisao.py
└── atividade_autonoma.py
```

Por padrão, ela usa o modelo definido em `config/llm.toml`; para isso, é necessária uma `GEMINI_API_KEY` pessoal configurada conforme o [guia de ambiente](../materiais/ambiente.md). O terminal informa:

```text
MODO ONLINE — GEMINI
```

Se precisar executar sem chave ou sem internet, acrescente `--offline`. Nesse modo, a decisão que representaria a LLM é simulada de modo explícito e reproduzível; o terminal informa `MODO OFFLINE — DECISÃO SIMULADA`:

```bash
uv run python praticas/encontro-03/02_ciclo_controlado.py --offline
```

A prática não grava nem mostra chaves.

## Missão 0 — Uma boa resposta já basta?

Uma pessoa escreve:

> “O projetor não funciona e a apresentação começa em breve.”

Execute:

```bash
uv run python praticas/encontro-03/01_uma_resposta.py
```

Leia a resposta antes de discutir sua arquitetura. Ela parece razoável, mas responda a estas perguntas:

- Qual objetivo orientou a resposta?
- Que informação o sistema ainda precisa obter?
- Quem decide o que fazer depois que a pessoa responder?
- Como o sistema saberia que terminou?

Uma resposta isolada pode ser uma interface útil. Porém, ela não deixa explícita uma trajetória: não há um estado que sobreviva à próxima mensagem, nem um mecanismo que conduza uma nova decisão.

O problema não é a qualidade do texto. É a ausência de uma responsabilidade de controle visível.

## Missão 1 — Faça a conversa virar um ciclo

O CampusBot agora recebe um objetivo mais específico: ajudar sem fingir que executou uma ação externa. Antes de rodar o programa, preveja a primeira escolha para o caso do projetor.

```bash
uv run python praticas/encontro-03/02_ciclo_controlado.py
```

Observe o registro. O agente pergunta pelo local, recebe uma resposta da pessoa simulada, atualiza o estado e então encerra a conversa explicando seu limite atual. Experimente o segundo caso:

```bash
uv run python praticas/encontro-03/02_ciclo_controlado.py acesso
```

### Leia o registro como uma cadeia de responsabilidades

No terminal, não compare a frase produzida com uma resposta “exata”. No modo com LLM, a redação pode variar. Compare as evidências que a arquitetura precisa preservar nos dois casos:

1. `DECISÃO` propõe uma das ações conversacionais permitidas;
2. `AGENTE` mostra a mensagem que realiza essa ação conversacional;
3. `NOVA PERCEPÇÃO` mostra a consequência observada no interlocutor simulado;
4. `ESTADO ATUAL` conserva a informação para a próxima decisão;
5. `PARADA` mostra que o controlador aceitou a conclusão ou aplicou seu limite de segurança.

No caso `acesso`, mudam objetivo, problema, urgência e local informado. A cadeia de responsabilidades continua a mesma. Isso é o que permite ao CampusBot tratar casos diferentes sem transformar cada conversa em uma sequência fixa de frases.

O programa não é um conjunto de frases em sequência. A cada passo, o controlador entrega ao componente de decisão:

```text
objetivo + percepção mais recente + estado disponível + ações permitidas
```

O componente devolve uma decisão estruturada:

```text
ação conversacional + mensagem + motivo + indicação de parada
```

O controlador verifica se a escolha respeita os limites e decide se deve terminar ou obter outra percepção. A LLM, quando usada, participa da decisão; ela não substitui sozinha o sistema que organiza o ciclo.

??? "Por que o exemplo termina sem abrir um chamado?"

    Porque o CampusBot desta prática ainda não possui uma ferramenta para consultar equipamentos, registrar um chamado ou alterar qualquer sistema externo. Dizer “chamado aberto” seria apenas uma afirmação em linguagem natural, não uma ação verificada no ambiente.

    Esse limite é deliberado. Neste encontro, investigamos os componentes e o ciclo de controle. No próximo, perguntaremos como o agente pode passar de responder para agir por meio de ferramentas e percepções do ambiente.

## O que entra em uma decisão agora?

Chamaremos de **contexto de decisão** o conjunto de informações que o sistema seleciona e entrega ao decisor naquela rodada. No CampusBot, ele reúne instruções de comportamento, objetivo, percepção mais recente, estado disponível e ações permitidas.

```text
instruções e limites
        + objetivo
        + percepção mais recente
        + estado selecionado
        + ações permitidas
        ↓
    contexto de decisão
        ↓
      próximo passo
```

Estado e contexto não são sinônimos. O estado é informação que o sistema conserva durante a execução; o contexto é o recorte que chega ao decisor agora. Nesta prática, o controlador entrega todo o estado disponível. Em sistemas maiores, ele pode selecionar apenas parte dele. No Encontro 05, investigaremos essa escolha com mais precisão.

## O modelo de componentes que a execução tornou necessário

O nome “agente baseado em LLM” não descreve uma peça única. Ele descreve uma organização na qual componentes com responsabilidades diferentes formam um ciclo.

```text
objetivo e limites
        ↓
percepção → estado disponível → decisão por modelo → próximo passo
    ↑                                                 ↓
ambiente ou interlocutor ← controlador ← validação e parada
```

No CampusBot, cada parte responde a uma pergunta diferente:

| Componente | Responsabilidade no exemplo | Pergunta que ajuda a fazer |
| --- | --- | --- |
| Objetivo | Delimita o que conta como ajuda neste caso. | O que o sistema tenta alcançar? |
| Percepção | Traz a mensagem inicial ou a nova resposta da pessoa. | O que acabou de mudar ou ficou conhecido? |
| Estado | Conserva, por exemplo, o local já informado. | O que o sistema já sabe nesta execução? |
| Contexto de decisão | Reúne o recorte de informações que chega ao decisor nesta rodada. | Do que a próxima escolha precisa saber agora? |
| Modelo de decisão | Propõe o próximo passo dentro das opções disponíveis. | Diante disso, o que faz sentido fazer agora? |
| Ações permitidas | Restringem o que pode ser escolhido: perguntar ou orientar. | O que este agente tem permissão para propor? |
| Controlador do ciclo | Entrega informações, valida a decisão e conduz a próxima etapa. | Quem mantém a execução coerente? |
| Condição de parada | Combina uma conclusão proposta com limites externos, como o máximo de passos. | Quando o sistema deve deixar de agir? |

Algumas arquiteturas juntam várias dessas responsabilidades em uma biblioteca; outras as distribuem por funções, serviços ou pessoas. A divisão concreta pode mudar. As responsabilidades continuam sendo úteis para analisar o sistema.

Também não há uma fronteira mágica em que todos os sistemas precisam conter exatamente as mesmas peças. Um chatbot de resposta única pode não precisar de ciclo. Um workflow pode manter estado e parar de modo explícito. O que importa aqui é reconhecer o que deve existir quando queremos que o sistema escolha próximos passos sucessivos em tempo de execução.

## Missão 2 — Quebre uma responsabilidade de propósito

Um agente não falha apenas porque a LLM “errou”. Execute uma versão deliberadamente defeituosa em modo controlado. Ela recebe novas mensagens, mas deixa de entregar ao decisor o estado atualizado.

```bash
uv run python praticas/encontro-03/03_diagnosticar_o_ciclo.py --sem-estado --offline
```

Antes de olhar a última linha, responda:

> Depois que a pessoa informa “É no Lab 4”, o que você espera que o agente faça no passo seguinte?

Nesta simulação, o agente volta a perguntar pelo local até atingir a parada de segurança. A nova percepção ocorreu, mas ela não foi preservada no estado entregue à decisão seguinte. A explicação não é “o modelo esqueceu” em sentido genérico: a experiência desligou a passagem entre percepção e estado que a política simulada consulta.

O modo controlado é importante: uma LLM também recebe a percepção mais recente — inclusive o texto “É no Lab 4” — e pode extrair dela o local mesmo quando o estado está incompleto. Se isso acontecer no modo padrão, não prova que o estado seja dispensável; mostra que duas fontes de informação chegaram ao decisor. Aqui queremos isolar uma fonte para tornar a falha diagnosticável.

Agora limite um ciclo que funciona:

```bash
uv run python praticas/encontro-03/03_diagnosticar_o_ciclo.py --limite 1 --offline
```

Nesse caso, a informação e a decisão podem estar corretas, mas o limite encerra a execução antes da segunda etapa. Limites de passos não demonstram inteligência; são um mecanismo de controle para evitar que um ciclo continue indefinidamente.

Essas duas experiências ainda não são um estudo completo de memória. Aqui, `estado` significa apenas a informação de trabalho necessária durante esta execução. No Encontro 05, investigaremos com mais precisão quais informações devem entrar no contexto, sobreviver entre etapas ou persistir além de uma conversa.

## Missão 3 — Quando uma decisão deve ser recusada?

Até agora, o CampusBot recebeu apenas decisões aceitáveis. Mas uma decisão estruturada não é automaticamente uma decisão executável. Antes de rodar, preveja: se o decisor propuser `abrir_chamado`, o que o controlador pode realmente fazer neste encontro?

```bash
uv run python praticas/encontro-03/04_validar_decisao.py
```

Depois, experimente uma incoerência diferente:

```bash
uv run python praticas/encontro-03/04_validar_decisao.py parada-incoerente
```

Esses comandos não chamam uma LLM. Eles entregam uma decisão bruta ao mesmo contrato que protege o ciclo para tornar a fronteira visível: o controlador recusa uma ação fora do conjunto permitido e também recusa uma combinação contraditória entre ação e parada. Nenhuma mensagem é enviada e nenhuma consequência é executada depois da recusa.

O modelo pode propor que a conversa terminou; o controlador ainda decide se essa proposta respeita o contrato e mantém um limite externo de passos. Assim, uma declaração de parada do modelo não é uma autorização ilimitada para encerrar ou continuar.

## O que a LLM faz — e o que ela não faz sozinha

No modo padrão, a LLM recebe objetivo, observação, estado e um conjunto pequeno de ações conversacionais. Ela devolve uma escolha em formato estruturado. O programa aceita apenas escolhas válidas e mantém o controle de continuar ou encerrar.

```bash
uv run python praticas/encontro-03/02_ciclo_controlado.py
```

Isso torna a LLM um componente de decisão sob restrições. Ela não ganha, por isso, acesso automático a e-mail, banco de dados, terminal, equipamentos ou sistemas institucionais. Tampouco garante que uma resposta esteja correta: o restante da arquitetura precisa definir informações, limites, validações e formas de observar consequências.

Com `--offline`, uma política preparada ocupa provisoriamente o lugar da LLM. A arquitetura continua visível porque a lição não é “o `if` virou uma LLM”; é que um sistema precisa organizar o que percebe, o que conserva, quem decide, quais escolhas aceita e como o ciclo termina.

## Síntese — o agente não cabe em uma chamada ao modelo

Reconstrua o percurso:

```text
uma resposta
→ não deixa clara a trajetória

objetivo + percepção + estado + decisão limitada
→ permite escolher um próximo passo

contexto selecionado + decisão validada
→ separa o que o modelo propõe do que o sistema aceita

controlador + consequência observável + parada
→ transforma decisões sucessivas em um ciclo controlado

sem estado ou sem limite
→ o comportamento pode repetir ou terminar na hora errada
```

Uma formulação útil para este momento é:

> **Uma LLM pode participar da decisão; um agente é o sistema que organiza decisões, informações, limites e consequências ao longo de uma trajetória.**

O CampusBot já conversa em mais de uma etapa, mas ainda não age sobre o ambiente. Ele pode pedir uma informação e orientar uma pessoa; não pode consultar a disponibilidade de outro projetor nem registrar um chamado. Essa é exatamente a tensão que abre o próximo encontro.

## Missão autônoma — Localize a responsabilidade que falta

Esta atividade é formativa e **sem nota**. Você pode iniciá-la no laboratório ou realizá-la em casa durante a semana. Não é necessário criar fork, branch, commit ou push.

Abra `praticas/encontro-03/atividade_autonoma.py`. Antes de alterar qualquer linha de código, preencha no próprio arquivo uma hipótese curta sobre um dos casos:

1. qual é o objetivo;
2. qual é a percepção inicial;
3. qual estado precisa sobreviver até a próxima decisão;
4. qual contexto de decisão chega ao modelo neste passo;
5. qual próximo passo o agente pode escolher;
6. como o controlador pode aceitar ou recusar a parada;
7. qual limite ainda existe porque não há ferramentas.

Em seguida, execute os dois casos controlados e compare o que mudou no problema com o que permaneceu na arquitetura:

```bash
uv run python praticas/encontro-03/atividade_autonoma.py projetor --offline
uv run python praticas/encontro-03/atividade_autonoma.py acesso --offline
uv run python praticas/encontro-03/03_diagnosticar_o_ciclo.py --sem-estado --offline
uv run python praticas/encontro-03/04_validar_decisao.py
```

Registre qual responsabilidade falhou na versão sem estado, qual linha do terminal sustenta sua conclusão e qual seria a menor mudança arquitetural para repará-la. No último comando, registre também qual regra fez o controlador recusar a decisão e qual consequência deixou de ocorrer. O modo padrão com LLM continua disponível para explorar o ciclo; aqui, `--offline` torna a comparação reproduzível.

Termine com a pergunta que abrirá o Encontro 04:

> **Que ferramenta ou capacidade externa o CampusBot precisaria ter para fazer mais do que responder?**
