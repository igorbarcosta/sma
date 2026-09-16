"""O ciclo explícito entre decisão, ferramenta, ambiente e nova decisão."""

from __future__ import annotations

import json
from typing import Any

from ambiente import retrato
from ferramentas import abrir_chamado, consultar_chamados
from modelo import decidir


def executar_ferramenta(ambiente: dict[str, Any], ferramenta: str, argumentos: dict[str, Any]) -> dict[str, Any]:
    """É o programa — e não o modelo — que chama a função escolhida."""
    if ferramenta == "consultar_chamados":
        return consultar_chamados(ambiente, argumentos["local"])
    if ferramenta == "abrir_chamado":
        return abrir_chamado(ambiente, argumentos["local"], argumentos["problema"])
    raise ValueError(f"Ferramenta desconhecida: {ferramenta}")


def executar_ciclo(
    pedido: str,
    ambiente: dict[str, Any],
    *,
    offline: bool = False,
    devolver_resultado: bool = True,
    limite_passos: int = 4,
) -> None:
    """Decida; responda ou execute; observe; então decida novamente."""
    observacoes: list[dict[str, Any]] = []
    print(f"[USUÁRIO]\n{pedido}")
    print(f"\n[AMBIENTE ANTES]\n{json.dumps(retrato(ambiente), ensure_ascii=False)}")
    for passo in range(1, limite_passos + 1):
        print(f"\n[CONTROLADOR] Passo {passo}: decidindo...")
        decisao = decidir(pedido, observacoes, offline)
        if decisao["tipo"] == "responder":
            print(f"\n[MODELO]\n{decisao['mensagem']}")
            print("\n[CONTROLADOR] O modelo decidiu responder. Encerrando o ciclo.")
            return
        ferramenta = decisao["ferramenta"]
        argumentos = decisao["argumentos"]
        print(f"\n[MODELO]\nQuero usar: {ferramenta}\nArgumentos: {json.dumps(argumentos, ensure_ascii=False)}")
        print("\n[CONTROLADOR]\nExecutando ferramenta...")
        print(f"\n[FERRAMENTA]\n{ferramenta}(...)")
        resultado = executar_ferramenta(ambiente, ferramenta, argumentos)
        print(f"\n[AMBIENTE DEPOIS]\n{json.dumps(retrato(ambiente), ensure_ascii=False)}")
        print(f"\n[RESULTADO DA FERRAMENTA]\n{json.dumps(resultado, ensure_ascii=False)}")
        if devolver_resultado:
            observacoes.append({"ferramenta": ferramenta, "resultado": resultado})
            print("\n[CONTROLADOR] O resultado foi devolvido ao modelo para a próxima decisão.")
        else:
            print("\n[CONTROLADOR] DEMONSTRAÇÃO: a ferramenta executou, mas o resultado não voltou ao modelo.")
    print("\n[CONTROLADOR] Parada de segurança: limite de passos atingido.")
