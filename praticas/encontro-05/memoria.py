"""Um arquivo JSON pequeno que pode sobreviver ao processo Python."""

import json
from pathlib import Path


def salvar_memoria(caminho, registro):
    Path(caminho).write_text(json.dumps(registro, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def recuperar_memoria(caminho):
    arquivo = Path(caminho)
    return json.loads(arquivo.read_text(encoding="utf-8")) if arquivo.exists() else None
