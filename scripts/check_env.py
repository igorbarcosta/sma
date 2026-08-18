from __future__ import annotations

import argparse
import importlib.metadata
import os
import platform
import subprocess
import sys
import tomllib
from pathlib import Path


EXPECTED_PYTHON = (3, 12)
EXPECTED_UV = "0.11.21"
EXPECTED_ZENSICAL = "0.0.53"
EXPECTED_GOOGLE_GENAI = "2.14.0"
REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
EXPECTED_ENVIRONMENT = (REPOSITORY_ROOT / ".venv").resolve()
LLM_CONFIG = REPOSITORY_ROOT / "config" / "llm.toml"


def status(ok: bool) -> str:
    return "OK" if ok else "ERRO"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Diagnostica o ambiente da disciplina.")
    parser.add_argument(
        "--check-api",
        action="store_true",
        help="faz uma chamada mínima e explícita à Gemini API",
    )
    return parser.parse_args()


def check_api(model: str, api_key: str) -> bool:
    try:
        from google import genai

        client = genai.Client(api_key=api_key)
        try:
            client.models.generate_content(
                model=model,
                contents="Responda somente com OK.",
            )
        finally:
            client.close()
    except Exception as error:  # A mensagem deliberadamente não expõe credenciais.
        print(f"Gemini API: falha ({type(error).__name__}).")
        print("Verifique a chave, a rede, a quota e a disponibilidade do modelo.")
        return False

    print(f"Gemini API: autenticação e modelo {model} disponíveis [OK]")
    return True


def main() -> int:
    args = parse_args()
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

    try:
        google_genai_version = importlib.metadata.version("google-genai")
    except importlib.metadata.PackageNotFoundError:
        google_genai_version = "não instalado"
    google_genai_ok = google_genai_version == EXPECTED_GOOGLE_GENAI

    with LLM_CONFIG.open("rb") as config_file:
        llm_config = tomllib.load(config_file)
    provider = llm_config["provider"]
    model = llm_config["model"]
    api_key = os.environ.get("GEMINI_API_KEY", "")

    print("Ambiente SMA — verificações locais")
    print(f"Python: {platform.python_version()} [{status(python_ok)}]")
    print(f"Ambiente: {sys.prefix} [{status(environment_ok)}]")
    print(f"uv: {uv_version} [{status(uv_ok)}]")
    print(f"Zensical: {zensical_version} [{status(zensical_ok)}]")
    print(f"google-genai: {google_genai_version} [{status(google_genai_ok)}]")
    print(f"Plataforma: {platform.system()} {platform.machine()}")
    print("\nCredencial e provider")
    print(f"Provider/modelo: {provider}/{model}")
    print(f"GEMINI_API_KEY: {'definida' if api_key else 'não definida'}")

    checks = [python_ok, environment_ok, uv_ok, zensical_ok, google_genai_ok]
    if not all(checks):
        print("Diagnóstico concluído: execute `uv sync --locked` e tente novamente.")
        return 1

    if args.check_api:
        if not api_key:
            print("Teste de API não executado: defina GEMINI_API_KEY.")
            return 1
        return 0 if check_api(model, api_key) else 1

    print("Diagnóstico local concluído: ambiente pronto.")
    if not api_key:
        print("Para usar a API, configure GEMINI_API_KEY conforme a documentação.")
    print("A API não foi chamada. Use `--check-api` para testar conectividade.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
