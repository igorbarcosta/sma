"""Liga decisão, ferramenta e estado; imprime as fronteiras da informação."""

import json

from ambiente import retrato
from contexto import montar_contexto
from estado import atualizar_estado
from ferramentas import abrir_chamado, consultar_chamados
from modelo import decidir


def mostrar(rotulo, valor):
    print(f"\n[{rotulo}]\n{json.dumps(valor, ensure_ascii=False, indent=2)}")


def executar(ambiente, estado, *, modo="adequado", offline=False, preservar=True, passos=3):
    print("MODO OFFLINE — DECISÃO SIMULADA" if offline else "MODO ONLINE — GEMINI")
    for passo in range(1, passos + 1):
        print(f"\n=== RODADA {passo} ===")
        mostrar("ESTADO ANTES", estado)
        contexto = montar_contexto(estado, modo)
        mostrar("CONTEXTO ENVIADO AO MODELO", contexto)
        mostrar("FICOU FORA", sorted(set(estado) - set(contexto)))
        decisao = decidir(contexto, offline)
        mostrar("DECISÃO", decisao)
        if decisao["tipo"] == "responder":
            return decisao
        ferramenta, args = decisao["ferramenta"], decisao["argumentos"]
        resultado = (consultar_chamados(ambiente, args["local"]) if ferramenta == "consultar_chamados"
                     else abrir_chamado(ambiente, args["local"], args["problema"]))
        mostrar("RESULTADO DA FERRAMENTA", resultado)
        mostrar("AMBIENTE", retrato(ambiente))
        if preservar:
            atualizar_estado(estado, ferramenta, resultado)
        else:
            print("[FALHA PLANEJADA] Resultado descartado antes da próxima rodada.")
        mostrar("ESTADO DEPOIS", estado)
    print("[PARADA] Limite de rodadas; nenhuma resposta final.")
    return None
