# Slides da disciplina

Os slides são escritos em Marp Markdown e derivados de roteiros pedagogicamente validados. Eles funcionam como instrumentos de condução dos encontros, não como resumos das páginas do site.

- fontes: `slides/encontro-XX-<slug>.md`;
- tema compartilhado: `slides/theme/sma.css`;
- distribuições oficiais versionadas: `slides/rendered/`;
- artefatos temporários: `.slides-build/`.

HTML e PDF são derivados das fontes e nunca devem ser editados manualmente. Notas do apresentador podem ser registradas em comentários HTML do fonte Marp.

## Comandos

```bash
npm run slides:preview
npm run slides:render -- encontro-XX-<slug>
npm run validate
```

O renderizador falha diante de slug inválido ou fonte inexistente e produz HTML e PDF somente em `slides/rendered/`. Depois de alterar um deck ou o tema, renderizar novamente e inspecionar visualmente todos os frames, verificando legibilidade, contraste, geometria e overflow.
