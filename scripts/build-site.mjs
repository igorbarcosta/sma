import { spawnSync } from "node:child_process";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repositoryRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const result = spawnSync("uv", ["run", "--locked", "zensical", "build", "--clean"], {
  cwd: repositoryRoot,
  stdio: "inherit",
});

if (result.error) {
  console.error(`Não foi possível executar o ambiente com uv: ${result.error.message}`);
  console.error("Instale uv 0.11.21 e execute: uv sync --locked");
  process.exit(1);
}

process.exit(result.status ?? 1);
