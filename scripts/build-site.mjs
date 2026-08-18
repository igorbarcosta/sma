import { existsSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repositoryRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const localZensical = resolve(repositoryRoot, ".venv/bin/zensical");
const executable = existsSync(localZensical) ? localZensical : "zensical";
const result = spawnSync(executable, ["build", "--clean"], {
  cwd: repositoryRoot,
  stdio: "inherit",
});

if (result.error) {
  console.error(`Não foi possível executar o Zensical: ${result.error.message}`);
  console.error("Instale as dependências com: python3.12 -m venv .venv && .venv/bin/python -m pip install -r requirements.txt");
  process.exit(1);
}

process.exit(result.status ?? 1);
