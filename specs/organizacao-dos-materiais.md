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

## Construção dos encontros

O roteiro pedagógico é a fonte do encontro. Antes dos slides, devem estar definidos e validados, na medida pertinente:

- problema ou necessidade que inicia a trajetória;
- resultados atendidos e dependências;
- operação cognitiva pretendida em cada atividade;
- evidência observável dessa operação;
- sequência de investigação, formalização, aplicação e transferência;
- grau de scaffolding e autonomia;
- núcleo necessário e possíveis aprofundamentos elásticos;
- relação com avaliações, desafios ou projeto, quando houver.

O encontro não precisa usar todos esses elementos como seções públicas. Detalhes internos de planejamento só devem aparecer ao estudante quando ajudarem a compreender, executar ou avaliar o próprio trabalho.

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

## Decisões ainda não tomadas

Permanecem fora desta spec até decisão posterior:

- framework agentivo ou biblioteca principal;
- gerenciador de ambiente e stack de implementação;
- tema visual final e taxonomia adicional;
- roteiros e composição detalhada de cada encontro;
- desafios e domínio concreto do projeto integrador;
- bibliografia.
