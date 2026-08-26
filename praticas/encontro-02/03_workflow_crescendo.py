from __future__ import annotations

import argparse

from suporte import buscar_caso, executar_acao


ORIENTACOES_CONHECIDAS = {
    "objeto_perdido": "Procure a recepção e informe o local onde viu o objeto pela última vez.",
    # Novo requisito da aula: climatização também terá orientação conhecida.
}


def escolher_acao(estado: dict) -> str:
    if not estado.get("local"):
        return "pedir_informacao"
    if estado["categoria"] == "internet" and estado["urgente"]:
        return "abrir_chamado_prioritario"
    if estado["categoria"] in ORIENTACOES_CONHECIDAS:
        return "fornecer_orientacao"
    if estado["categoria"] in {"internet", "computador", "climatizacao"}:
        return "abrir_chamado_normal"
    return "encaminhar_para_humano"


parser = argparse.ArgumentParser()
parser.add_argument("caso", nargs="?", default="mochila-perdida")
args = parser.parse_args()

caso = buscar_caso(args.caso)
acao = escolher_acao(caso["estado"])
print(f"MENSAGEM: {caso['mensagem']}")
print(f"WORKFLOW ESCOLHEU: {acao}")
if acao == "fornecer_orientacao":
    print(f"ORIENTAÇÃO: {ORIENTACOES_CONHECIDAS[caso['estado']['categoria']]}")
executar_acao(acao)
