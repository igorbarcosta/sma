# Encontro 06 — Revisão com LangChain e discussão dos projetos

Neste encontro, retomaremos os conceitos de agente, ferramentas, ciclo de execução, estado e memória construindo um agente com LangChain. Depois, discutiremos as propostas do projeto integrador a partir da leitura dos fluxos enviados.

## 1. Revisão: construir e observar um agente

Abra o notebook [Nosso primeiro agente com LangChain no Google Colab](https://colab.research.google.com/drive/1mT_AgE2NKYTz1BtEupdWEVWAF6Y3r7mh). O acesso está disponível somente com o e-mail institucional do IFPB. Antes de começar, faça sua própria cópia em **Arquivo → Salvar uma cópia no Drive** e trabalhe nela.

Na preparação, configure sua própria `GEMINI_API_KEY` no painel **Secrets** e permita o acesso pelo notebook. Execute as células na ordem indicada; as instruções de instalação e configuração estão no próprio documento.

A construção parte de um agente sem ferramentas e acrescenta abertura e consulta de chamados, observação da trajetória e memória de curto prazo. Antes das execuções sinalizadas no notebook, faça uma previsão; depois, compare-a com as mensagens e com o estado do ambiente.

Durante a revisão, observe:

- quem solicita a ferramenta, quem a executa e o que realmente mudou no ambiente;
- como o resultado de uma consulta orienta a próxima ação;
- como a trajetória distingue uma solicitação, uma execução e uma ação bem-sucedida;
- o que é lembrado na mesma conversa e o que muda ao usar outra `thread_id`.

Ao retomar o material, use os experimentos de chamado existente, capacidade ausente e ferramenta indisponível para explicar o comportamento observado. O framework conduz parte do ciclo, mas as responsabilidades arquiteturais continuam presentes.

## 2. Discussão das propostas de projeto

O PDF [Sprint 0 — Fluxos e discussão das propostas](../projeto/materiais/sprint0_fluxos_projetos.pdf) reúne a leitura dos projetos enviados, os fluxos compreendidos e perguntas para cada grupo.

Na discussão, confira se o fluxo representado corresponde à proposta e retome as perguntas do seu projeto: qual é a solução mais simples que serve de comparação, onde existe decisão dinâmica e que evidência permitiria justificar uma arquitetura agentiva ou multiagente?

As sugestões de primeiro teste no PDF servirão de apoio à conversa sobre escopo e avaliação. Para retomar o encontro, consulte o trecho do seu projeto junto das observações feitas na discussão. Prazos e entregas permanecem no Google Classroom.
