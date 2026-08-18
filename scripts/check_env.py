from __future__ import annotations

import importlib.metadata
import platform
import subprocess
import sys
from pathlib import Path


EXPECTED_PYTHON = (3, 12)
EXPECTED_UV = "0.11.21"
EXPECTED_ZENSICAL = "0.0.53"
REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
EXPECTED_ENVIRONMENT = (REPOSITORY_ROOT / ".venv").resolve()


def status(ok: bool) -> str:
    return "OK" if ok else "ERRO"


def main() -> int:
    python_ok = sys.version_info[:2] == EXPECTED_PYTHON
    environment_ok = Path(sys.prefix).resolve() == EXPECTED_ENVIRONMENT

    try:
        uv_output = subprocess.run(
            ["uv", "--version"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        uv_version = uv_output.split()[1]
    except (FileNotFoundError, subprocess.CalledProcessError):
        uv_version = "não disponível"
    uv_ok = uv_version == EXPECTED_UV

    try:
        zensical_version = importlib.metadata.version("zensical")
    except importlib.metadata.PackageNotFoundError:
        zensical_version = "não instalado"
    zensical_ok = zensical_version == EXPECTED_ZENSICAL

    print("Ambiente SMA")
    print(f"Python: {platform.python_version()} [{status(python_ok)}]")
    print(f"Ambiente: {sys.prefix} [{status(environment_ok)}]")
    print(f"uv: {uv_version} [{status(uv_ok)}]")
    print(f"Zensical: {zensical_version} [{status(zensical_ok)}]")
    print(f"Plataforma: {platform.system()} {platform.machine()}")

    checks = [python_ok, environment_ok, uv_ok, zensical_ok]
    if all(checks):
        print("Diagnóstico concluído: ambiente pronto.")
        return 0

    print("Diagnóstico concluído: execute `uv sync --locked` e tente novamente.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
