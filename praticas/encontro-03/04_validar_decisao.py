from __future__ import annotations

import argparse
import json

from modelo import validar_decisao


DECISOES_INVALIDAS = {
    "acao-desconhecida": {
        "acao": "abrir_chamado",
        "mensagem": "Vou abrir um chamado agora.",
        "concluiu": True,
        "motivo": "parece uma boa ideia",
    },
    "parada-incoerente": {
        "acao": "perguntar_local",
        "mensagem": "Em qual local isso está acontecendo?",
        "concluiu": True,
        "motivo": "quero encerrar mesmo precisando de uma resposta",
    },
}


parser = argparse.ArgumentParser(description="Mostra o controlador recusando uma decisão fora do contrato.")
parser.add_argument("violacao", nargs="?", choices=DECISOES_INVALIDAS, default="acao-desconhecida")
args = parser.parse_args()

decisao_bruta = DECISOES_INVALIDAS[args.violacao]
print(f"DECISÃO BRUTA: {json.dumps(decisao_bruta, ensure_ascii=False)}")

try:
    validar_decisao(decisao_bruta)
except ValueError as erro:
    print(f"DECISÃO RECUSADA: {erro}")
    print("CONSEQUÊNCIA: nenhuma mensagem foi enviada e nenhuma ação externa foi executada.")
else:
    raise RuntimeError("Esta demonstração deveria conter uma decisão inválida.")
