import { existsSync, readdirSync, statSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { dirname, extname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repositoryRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const requiredFiles = [
  "zensical.toml",
  "pyproject.toml",
  "uv.lock",
  ".python-version",
  ".devcontainer/Dockerfile",
  ".devcontainer/devcontainer.json",
  "scripts/check_env.py",
  "docs/index.md",
  "docs/plano-de-ensino.md",
  "docs/cronograma.md",
  "docs/encontros/index.md",
  "docs/desafios/index.md",
  "docs/projeto/index.md",
  "docs/materiais/index.md",
  "docs/materiais/referencias.md",
  "slides/render.mjs",
  "slides/theme/sma.css",
];

const errors = [];

for (const relativePath of requiredFiles) {
  if (!existsSync(resolve(repositoryRoot, relativePath))) {
    errors.push(`Arquivo obrigatório ausente: ${relativePath}`);
  }
}

const slidesDirectory = resolve(repositoryRoot, "slides");
const renderedDirectory = resolve(slidesDirectory, "rendered");
const slideMarkdownFiles = readdirSync(slidesDirectory, { withFileTypes: true })
  .filter((entry) => entry.isFile() && entry.name.endsWith(".md"))
  .map((entry) => entry.name);
const invalidSourceNames = slideMarkdownFiles.filter(
  (name) => name !== "README.md" && !/^encontro-\d{2}-[a-z0-9-]+\.md$/.test(name),
);
for (const name of invalidSourceNames) {
  errors.push(`Fonte de slides fora da convenção: slides/${name}`);
}
const sourceSlugs = new Set(
  slideMarkdownFiles
    .filter((name) => /^encontro-\d{2}-[a-z0-9-]+\.md$/.test(name))
    .map((name) => name.slice(0, -3)),
);

const renderedFiles = readdirSync(renderedDirectory, { withFileTypes: true })
  .filter((entry) => entry.isFile() && [".html", ".pdf"].includes(extname(entry.name)))
  .map((entry) => entry.name);
const renderedSlugs = new Set(renderedFiles.map((name) => name.replace(/\.(html|pdf)$/, "")));

for (const slug of sourceSlugs) {
  for (const extension of ["html", "pdf"]) {
    if (!existsSync(resolve(renderedDirectory, `${slug}.${extension}`))) {
      errors.push(`Distribuição ausente para ${slug}: slides/rendered/${slug}.${extension}`);
    }
  }
}

for (const slug of renderedSlugs) {
  if (!sourceSlugs.has(slug)) {
    errors.push(`Distribuição órfã sem fonte: ${slug}`);
  }
}

for (const name of renderedFiles) {
  if (statSync(resolve(renderedDirectory, name)).size === 0) {
    errors.push(`Distribuição vazia: slides/rendered/${name}`);
  }
}

for (const slug of renderedSlugs) {
  for (const extension of ["html", "pdf"]) {
    if (!existsSync(resolve(renderedDirectory, `${slug}.${extension}`))) {
      errors.push(`Par de distribuição incompleto para ${slug}: falta ${extension.toUpperCase()}`);
    }
  }
}

if (errors.length > 0) {
  for (const error of errors) console.error(error);
  process.exit(1);
}

const environmentCheck = spawnSync(
  "uv",
  ["run", "--locked", "python", resolve(repositoryRoot, "scripts/check_env.py")],
  { cwd: repositoryRoot, stdio: "inherit" },
);

if (environmentCheck.error) {
  console.error(`Falha ao iniciar diagnóstico do ambiente: ${environmentCheck.error.message}`);
  process.exit(1);
}

if (environmentCheck.status !== 0) process.exit(environmentCheck.status ?? 1);

const build = spawnSync(process.execPath, [resolve(repositoryRoot, "scripts/build-site.mjs")], {
  cwd: repositoryRoot,
  stdio: "inherit",
});

if (build.error) {
  console.error(`Falha ao iniciar build do site: ${build.error.message}`);
  process.exit(1);
}

if (build.status !== 0) process.exit(build.status ?? 1);

console.log(`Validação concluída: ${sourceSlugs.size} deck(s), ${renderedFiles.length} distribuição(ões).`);
