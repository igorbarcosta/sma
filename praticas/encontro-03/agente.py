from __future__ import annotations

from typing import Any

from casos import buscar_caso
from modelo import decidir


def _registrar_resposta(caso: dict[str, Any], estado: dict[str, Any]) -> str:
    """Simula a próxima percepção; não é uma ferramenta nem altera sistema externo."""
    if caso["respostas"]:
        resposta = caso["respostas"].pop(0)
        caso["ultima_resposta"] = resposta
    else:
        # Quando o agente repete a mesma pergunta, a pessoa simulada repete a resposta.
        # Isso torna visível que a falha está em preservar o estado, não na percepção.
        resposta = caso["ultima_resposta"]

    if "Lab 4" in resposta:
        estado["local"] = "Lab 4"
    elif "laboratório de redes" in resposta:
        estado["local"] = "laboratório de redes"
    return resposta


def executar_ciclo(
    caso_id: str,
    *,
    online: bool = False,
    manter_estado: bool = True,
    limite_passos: int = 4,
) -> None:
    caso = buscar_caso(caso_id)
    objetivo = caso["objetivo"]
    estado: dict[str, Any] = caso["estado_inicial"]
    observacao = caso["mensagem_inicial"]

    print(f"OBJETIVO: {objetivo}")
    print(f"PERCEPÇÃO INICIAL: {observacao}")
    print(f"ESTADO INICIAL: {estado}")

    for passo in range(1, limite_passos + 1):
        estado_para_decisao = estado if manter_estado else caso["estado_inicial"]
        decisao = decidir(objetivo, observacao, estado_para_decisao, online=online)
        print(f"\nPASSO {passo}")
        print(f"DECISÃO: {decisao['acao']}")
        print(f"MOTIVO: {decisao['motivo']}")
        print(f"AGENTE: {decisao['mensagem']}")

        if decisao["concluiu"]:
            print("\nPARADA: o componente de decisão declarou que o objetivo conversacional foi atendido.")
            return

        if decisao["acao"] == "perguntar_local":
            observacao = _registrar_resposta(caso, estado if manter_estado else {})
            print(f"NOVA PERCEPÇÃO: {observacao}")
            print(f"ESTADO ATUAL: {estado}")
            continue

        raise RuntimeError("O controlador não sabe como continuar após esta decisão.")

    print("\nPARADA DE SEGURANÇA: o limite de passos foi atingido antes da conclusão.")
