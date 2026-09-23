"""Três defeitos pequenos para localizar, corrigir e justificar com evidência."""

import argparse

from ambiente import criar_ambiente
from controlador import executar, mostrar
from estado import criar_estado
from modelo import responder_sobre_protocolo


def preparar(caso):
    estado = criar_estado()
    ambiente = criar_ambiente()
    if caso == "estado":
        return ambiente, estado, "adequado", False
    if caso == "contexto":
        estado["ultima_consulta"] = {"ok": True, "chamados": []}
        return ambiente, estado, "de_menos", True  # TROQUE apenas o recorte, depois compare.
    estado["memoria"] = {"protocolo": "CH-001", "status": "aberto"}
    ambiente = criar_ambiente([{"protocolo": "CH-001", "local": "Lab 4", "problema": "projetor não funciona", "status": "encerrado"}])
    return ambiente, estado, "memoria", True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("caso", choices=("estado", "contexto", "memoria"))
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    ambiente, estado, modo, preservar = preparar(args.caso)
    if args.caso == "memoria":
        mostrar("AMBIENTE ATUAL", ambiente["chamados"])
        mostrar("MEMÓRIA ANTIGA", estado["memoria"])
        print("[RESPOSTA] " + responder_sobre_protocolo({"memoria": estado["memoria"]}))
        # Intervenção: consulte o ambiente e corrija a informação usada na resposta.
    else:
        executar(ambiente, estado, modo=modo, preservar=preservar, offline=args.offline, passos=2)


if __name__ == "__main__":
    main()
