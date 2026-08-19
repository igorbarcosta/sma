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

A página pública de cada encontro é material de aprendizagem e revisão autônoma. Ela deve ensinar pelo texto e permitir que o estudante reconstrua o raciocínio, compreenda os conceitos e estude posteriormente, inclusive quando não tiver participado de toda a experiência presencial. Não deve ser transcrição dos slides, roteiro do professor, lista de atividades nem resumo telegráfico.

Os slides são instrumentos de condução da experiência presencial. Preservam o arco narrativo por meio de casos, perguntas, contrastes, revelações e progressão visual, enquanto as explicações detalhadas permanecem na página pública.

O planejamento pedagógico sustenta ambos e contém intenção, operação cognitiva, evidência observável, timing, concepções esperadas e decisões de condução. Esses elementos não devem aparecer mecanicamente no texto do estudante: devem ser traduzidos em perguntas, orientações e explicações naturais. Essa separação é de função e não exige, por si só, um novo artefato público.

## Construção dos encontros

O roteiro pedagógico é a fonte do encontro. Antes dos slides, devem estar definidos e validados, na medida pertinente:

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

## Slides

Os slides são derivados de um roteiro pedagogicamente validado e funcionam como instrumento de condução. Não devem ser uma conversão mecânica da página em tópicos.

- `slides/*.md` será a fonte da verdade em Marp;
- `slides/theme/` conterá o tema compartilhado;
- `slides/rendered/` conterá HTML e PDF oficiais derivados e versionados;
- renderizados nunca serão editados manualmente;
- alterações no fonte ou tema exigirão nova renderização e inspeção visual.

SMA deve reaproveitar a base visual madura de POO, adaptando identidade e semântica. Inicialmente, preservar apenas categorias genéricas quando tiverem função real:

- Pergunta;
- Conceito;
- Atividade;
- Atenção/Armadilha;
- Síntese;
- Ideia-chave/Takeaway.

Não inventar uma taxonomia visual extensa. Categorias adicionais, como Evidência ou Decisão Arquitetural, só devem surgir quando justificadas pelo desenho real dos materiais. Perguntas ou exemplos narrativos comuns não precisam virar categorias visuais.

## Legibilidade

- Usar linguagem técnica clara e direta.
- Preferir uma trajetória causal a uma lista de assuntos.
- Manter exemplos próximos das ideias que ajudam a compreender.
- Evitar paredes de texto, listas extensas e destaques sem função semântica.
- Em slides, trabalhar uma ideia principal por frame e preservar legibilidade a distância.
- Diante de excesso, revisar densidade e divisão antes de reduzir fonte.
- Usar notas do apresentador para orientações de condução que não precisem permanecer projetadas.

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
