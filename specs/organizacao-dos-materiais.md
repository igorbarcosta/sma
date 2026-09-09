# Organização dos encontros e materiais

Este documento registra como o tempo da disciplina e seus materiais permanentes devem ser organizados. Não define o roteiro de nenhum encontro.

## Organização temporal

A disciplina possui 14 quartas-feiras, com quatro tempos de 50 minutos por quarta. Cada quarta constitui um encontro, mas não uma aula expositiva de 200 minutos.

Como referência flexível:

- aproximadamente dois tempos presenciais podem ser conduzidos pelo professor;
- um terceiro tempo pode funcionar como estúdio assistido ou flexível quando houver necessidade;
- o tempo restante será trabalho autônomo guiado e poderá, quando apropriado, ocorrer fora da sala;
- a proporção presencial e autônoma pode mudar ao longo do semestre à medida que a autonomia aumenta.

Essa referência não é um template rígido. Não adotar a estrutura fixa `Aula → Laboratório` nem criar séries independentes de aulas e laboratórios.

### Trabalho autônomo orientado

O trabalho autônomo orientado faz parte da organização regular da disciplina. É formativo e sem nota por padrão e não deve ser confundido com Desafio, Avaliação ou Projeto. Se uma atividade compuser a nota, ela deverá ser explicitamente apresentada como um desses instrumentos avaliativos, de acordo com a arquitetura de avaliação da disciplina.

Ele pode ser realizado no laboratório ou em casa, conforme a preferência e a necessidade do estudante, sem diferença pedagógica entre os locais. Normalmente, será desenvolvido ao longo da semana e concluído antes do encontro seguinte. Essa flexibilidade não deve ser descrita como um “4º tempo remoto”, pois não estabelece modalidade nem regra de frequência e não transforma os quatro tempos em uma divisão rígida.

Cada trabalho autônomo deve declarar a operação cognitiva pretendida — por exemplo, consolidar, transferir, investigar, comparar, formular hipótese ou preparar o próximo encontro — e evitar tarefas genéricas apresentadas apenas como dever de casa. Quando houver trabalho autônomo, o encontro seguinte deve procurar reutilizar brevemente e de modo intencional o resultado produzido. A duração deve ser realista, compatível com a carga semanal e sem criar sobrecarga.

A continuidade semanal pode ser representada conceitualmente como:

```text
encontro
→ problema / investigação / formalização / prática
→ trabalho autônomo orientado
→ laboratório OU casa
→ realização ao longo da semana
→ retomada breve no encontro seguinte
```

Essa sequência descreve a organização pedagógica do trabalho. Ela não define nem altera automaticamente regras institucionais de frequência. Questões administrativas de presença permanecem separadas e só devem ser registradas quando houver decisão institucional específica.

## Unidade pública

Os materiais públicos dos encontros usarão futuramente:

```text
docs/encontros/encontro-XX-<slug>.md
```

- `XX` possui dois dígitos;
- o slug usa letras minúsculas, números e hífens;
- datas e semestre não pertencem ao nome permanente da página;
- cada página deve representar a trajetória do encontro, não apenas reunir tópicos;
- a composição entre condução presencial, estúdio e trabalho autônomo deve responder ao desenho real do encontro.

Não criar os 14 arquivos antes de seus desenhos pedagógicos estarem definidos.

## Conteúdo público permanente

A futura navegação pública terá:

- Início;
- Plano de Ensino;
- Cronograma;
- Encontros, contendo os 14 encontros;
- Desafios;
- Projeto;
- Materiais.

O site conterá conteúdo e orientações permanentes. O Google Classroom será usado operacionalmente para entregas, prazos, comunicação e notas. Evitar duplicar no site informações voláteis que pertencem ao Classroom.

Desafios e projeto possuirão páginas permanentes, mas seus casos concretos só devem ser criados quando solicitados e pedagogicamente definidos.

### Funções dos materiais

A página pública de cada encontro é material completo de aprendizagem e revisão autônoma, desenvolvido em texto narrativo. Ela deve ensinar pelo texto e permitir que o estudante reconstrua o raciocínio, compreenda os conceitos e estude posteriormente, inclusive quando não tiver participado da condução presencial. Não deve ser roteiro do professor, lista de atividades nem resumo telegráfico.

Cada novo encontro terá uma prática em `praticas/encontro-XX/`. Quando a experiência depender de observar ou modificar um sistema, o artefato executável ocupa o centro da investigação e o roteiro público funciona como guia de estudo, execução e interpretação. Roteiro e prática constituem juntos o material completo.

A disciplina não criará slides para novos encontros. O acervo histórico pode permanecer publicado, mas não é pré-requisito nem fonte de verdade para novos materiais. O planejamento pedagógico sustenta roteiro e prática e contém intenção, operação cognitiva, evidência observável, timing, concepções esperadas e decisões de condução. Esses elementos não devem aparecer mecanicamente no texto do estudante: devem ser traduzidos em perguntas, orientações e explicações naturais.

Um roteiro autoguiado precisa declarar o problema, a preparação necessária, os comandos executáveis, o que observar, perguntas que orientem a interpretação, análises posteriores e a próxima ação. A prática precisa produzir evidências que o estudante consiga relacionar a essas perguntas. O estudante não deve depender de explicação oral, de um slide ou de uma intervenção do professor para descobrir como começar, interpretar a saída ou recuperar o percurso.

## Construção dos encontros

O roteiro pedagógico é a fonte do encontro. Antes de produzir o roteiro público e a prática, devem estar definidos e validados, na medida pertinente:

- problema ou necessidade que inicia a trajetória;
- narrativa conceitual causal que conecta tensões, investigações, formalizações, exemplos e transferências;
- resultados atendidos e dependências;
- operação cognitiva pretendida em cada atividade;
- evidência observável dessa operação;
- sequência de investigação, formalização, aplicação e transferência;
- grau de scaffolding e autonomia;
- núcleo necessário e possíveis aprofundamentos elásticos;
- relação com avaliações, desafios ou projeto, quando houver.

O encontro não precisa usar todos esses elementos como seções públicas. Detalhes internos de planejamento só devem aparecer ao estudante quando ajudarem a compreender, executar ou avaliar o próprio trabalho, sem rótulos como `Operação cognitiva` ou `Evidência`.

## Acervo histórico de slides

Os decks existentes em `slides/` e suas distribuições podem ser preservados como registro dos encontros já preparados. Não criar, derivar ou atualizar decks para novos encontros. Uma correção pontual em um deck histórico só é adequada quando corrige erro factual em material já publicado e exige nova renderização do artefato correspondente.

## Legibilidade

- Usar linguagem técnica clara e direta.
- Preferir uma trajetória causal a uma lista de assuntos.
- Manter exemplos próximos das ideias que ajudam a compreender.
- Evitar paredes de texto, listas extensas e destaques sem função semântica.
- No roteiro, dividir explicações, comandos, perguntas e análises para que a sequência permaneça navegável e autoguiada.
- Na prática, preferir saídas observáveis, casos sintéticos e passos que possam ser repetidos; quando houver alternativas ou falhas comuns, explicá-las no roteiro.

## Ambiente técnico de referência

- Python 3.12 é a versão-base da disciplina.
- `uv` gerencia o projeto, o ambiente virtual e as dependências.
- `pyproject.toml` declara o projeto e suas dependências; `uv.lock` fixa a resolução reproduzível.
- Clone local e GitHub Codespaces são ambientes oficialmente suportados.
- Codespaces é uma alternativa para dificuldades de configuração local, não um requisito.
- O ambiente local deve permanecer plenamente funcional e não depender de Codespaces.
- Materiais que dependam de execução devem ser testados nos dois ambientes.
- Os comandos usados nos materiais devem ser equivalentes localmente e no Codespaces.
- Evitar dependências técnicas que não contribuam para os resultados de aprendizagem.
- Não manter listas paralelas de dependências fora de `pyproject.toml` e `uv.lock`.

### Provider didático padrão

- A Gemini API é o provider didático padrão inicial dos encontros.
- `gemini-3.5-flash-lite` é o modelo inicial de referência, registrado uma única vez na configuração operacional.
- O acesso em Python usa o SDK atual `google-genai`; não usar o SDK legado `google-generativeai`.
- Provider e modelo são escolhas operacionais substituíveis, não conceitos curriculares. Os materiais conceituais não devem depender semanticamente do Gemini.
- Exemplos futuros devem evitar espalhar configuração específica do provider, sem criar interface genérica, adapter, factory ou framework próprio de abstração.
- Cada estudante usa sua própria `GEMINI_API_KEY`. Não haverá credencial compartilhada da turma nem segredo incluído no repositório.
- Outros providers podem ser usados posteriormente para comparação ou no projeto integrador.
- Exercícios didáticos e materiais oficiais devem usar dados sintéticos ou controlados, nunca dados pessoais, institucionais, confidenciais ou sensíveis.

## Decisões ainda não tomadas

Permanecem fora desta spec até decisão posterior:

- framework agentivo ou biblioteca principal além do SDK de acesso ao provider;
- stack de implementação além de Python, `uv` e do acesso operacional à Gemini API;
- tema visual final e taxonomia adicional;
- roteiros e composição detalhada de cada encontro;
- desafios e domínio concreto do projeto integrador;
- bibliografia.
