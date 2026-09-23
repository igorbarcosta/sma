# CampusBot — Encontro 05

Os chamados são sintéticos. `ambiente.py` guarda a realidade do sistema de chamados; `estado.py` guarda informação da execução; `contexto.py` escolhe o que entra na decisão; `memoria.py` grava e lê um JSON. `modelo.py` recebe apenas o contexto e decide; `controlador.py` executa as ferramentas. `cenarios.py` prepara as nove variações. Os arquivos numerados são entradas curtas para cada experiência.

Execute da raiz do repositório com `uv run python praticas/encontro-05/NN_nome.py --offline`. `--offline` usa um decisor simulado e declarado, sem rede; sem a opção, o ciclo principal usa Gemini e exige `GEMINI_API_KEY`. Compare as saídas do modo offline antes de explorar o modelo real, cuja saída pode variar.

| Arquivo | Pergunta que testa |
| --- | --- |
| `01_esqueceu_o_resultado.py` | O que acontece quando o resultado não é guardado? |
| `02_estado_entre_passos.py` | Qual pequena mudança permite avançar? |
| `03_contexto_demais.py` | Tudo que o sistema sabe precisa entrar na decisão? |
| `04_contexto_de_menos.py` | O que se perde quando a consulta fica fora? |
| `05_comparacao_ab.py` | Mesmo decisor, objetivo e estado: o recorte muda a ação? |
| `06_informacao_desatualizada.py` | Uma consulta antiga ainda descreve o ambiente? |
| `07_informacao_conflitante.py` | O local antigo ou a correção recente orienta a ação? |
| `08_memoria_entre_execucoes.py` | O que sobrevive a um novo processo? |
| `09_memoria_desatualizada.py` | Lembrar um status antigo pode induzir erro? |

Para observar dois **processos diferentes** usando um arquivo escolhido por você:

```bash
uv run python praticas/encontro-05/08_memoria_entre_execucoes.py --fase gravar --arquivo /tmp/campusbot-encontro-05.json --offline
uv run python praticas/encontro-05/08_memoria_entre_execucoes.py --fase recuperar --arquivo /tmp/campusbot-encontro-05.json --offline
```

O segundo processo começa com estado novo. Caso execute `recuperar` antes de `gravar`, a lembrança estará ausente. O arquivo é local, contém somente dados fictícios e pode ser descartado quando terminar.

## Duas intervenções pequenas

1. Em `contexto.py`, observe o modo `de_menos` e corrija o recorte que vai ao decisor. Rode o A/B antes e depois. Registre qual campo entrou, qual decisão mudou e por quê. Restaure o defeito para repetir o experimento original.
2. Em `atividade_autonoma.py`, caso `memoria`, consulte o ambiente antes de afirmar o status. Mostre a resposta antiga e a resposta depois da consulta. Não é necessário criar uma política geral de atualização.

## Trabalho autônomo orientado

Execute `atividade_autonoma.py` para os casos `estado`, `contexto` e `memoria`, sempre com `--offline`. Para cada caso, escreva: hipótese, linha da saída que mostra o defeito, menor correção, nova saída e justificativa. A tarefa é formativa e sem nota por padrão.
