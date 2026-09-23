"""Nove variações curtas do mesmo CampusBot e do mesmo sistema de chamados."""

import argparse
import tempfile
from pathlib import Path

from ambiente import criar_ambiente
from contexto import montar_contexto
from controlador import executar, mostrar
from estado import criar_estado
from memoria import recuperar_memoria, salvar_memoria
from modelo import PROMPT_BASE, responder_sobre_protocolo


def chamado(local="Lab 4", status="aberto"):
    return {"protocolo": "CH-001", "local": local, "problema": "projetor não funciona", "status": status}


def executar_cenario(numero, offline, caminho, fase="recuperar"):
    if numero in {1, 2, 3, 4}:
        modos = {1: ("adequado", False, 2), 2: ("adequado", True, 3),
                 3: ("demais", True, 3), 4: ("de_menos", True, 2)}
        modo, preservar, passos = modos[numero]
        executar(criar_ambiente(), criar_estado(), modo=modo, offline=offline,
                 preservar=preservar, passos=passos)
    elif numero == 5:
        print("[CONTROLE A/B] Mesmo modelo, prompt, objetivo, ferramentas e estado inicial.")
        print(f"[PROMPT BASE] {PROMPT_BASE}")
        for nome, modo in (("A — insuficiente", "de_menos"), ("B — adequado", "adequado")):
            print(f"\n===== AGENTE {nome} =====")
            estado = criar_estado()
            estado["ultima_consulta"] = {"ok": True, "chamados": []}
            executar(criar_ambiente(), estado, modo=modo, offline=offline, passos=1)
    elif numero == 6:
        ambiente = criar_ambiente([chamado()])
        estado = criar_estado()
        estado["ultima_consulta"] = {"ok": True, "chamados": []}
        print("[MUDANÇA NO AMBIENTE] Depois da consulta antiga, CH-001 apareceu.")
        executar(ambiente, estado, offline=offline, passos=1)
        print("[NOVA TENTATIVA] Descartar a consulta antiga e verificar de novo.")
        estado = criar_estado()
        executar(criar_ambiente([chamado()]), estado, offline=offline, passos=2)
    elif numero == 7:
        for titulo, corrigir in (("local antigo", False), ("nova percepção", True)):
            print(f"\n===== {titulo.upper()} =====")
            ambiente = criar_ambiente([chamado("Lab 5")])
            estado = criar_estado()
            mostrar("NOVA PERCEPÇÃO", {"local": "Lab 5"})
            if corrigir:
                estado["local"] = "Lab 5"
            executar(ambiente, estado, offline=offline, passos=3)
    elif numero == 8:
        if caminho is None:
            raise ValueError("Informe --arquivo para preservar a lembrança entre processos.")
        if fase == "gravar":
            estado = criar_estado()
            executar(criar_ambiente(), estado, offline=offline, passos=3)
            registro = {"local": "Lab 4", "problema": "projetor", "protocolo": estado["ultima_abertura"]["protocolo"], "status": "aberto"}
            salvar_memoria(caminho, registro)
            mostrar("MEMÓRIA SALVA", registro)
        else:
            estado = criar_estado()
            mostrar("NOVA EXECUÇÃO — ESTADO INICIAL", estado)
            print("[SEM MEMÓRIA] " + responder_sobre_protocolo(montar_contexto(estado, "memoria")))
            estado["memoria"] = recuperar_memoria(caminho)
            mostrar("MEMÓRIA RECUPERADA", estado["memoria"])
            print("[COM MEMÓRIA] " + responder_sobre_protocolo(montar_contexto(estado, "memoria")))
    elif numero == 9:
        # Arquivo temporário exclusivo deste experimento; não altera a memória do 08.
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = Path(pasta) / "memoria.json"
            salvar_memoria(arquivo, {"local": "Lab 4", "problema": "projetor", "protocolo": "CH-001", "status": "aberto"})
            ambiente = criar_ambiente([chamado(status="encerrado")])
            estado = criar_estado()
            estado["memoria"] = recuperar_memoria(arquivo)
            mostrar("MEMÓRIA", estado["memoria"])
            mostrar("AMBIENTE ATUAL", ambiente["chamados"])
            print("[RESPOSTA COM LEMBRANÇA ANTIGA] " + responder_sobre_protocolo(montar_contexto(estado, "memoria")))
            print("[INTERVENÇÃO 2] Consulte o ambiente antes de afirmar o status atual.")
            # A pequena correção é explícita: atualizar o registro com a observação atual.
            from ferramentas import consultar_chamados
            atuais = consultar_chamados(ambiente, "Lab 4")["chamados"]
            if atuais:
                estado["memoria"]["status"] = atuais[0]["status"]
            print("[RESPOSTA APÓS CONFERÊNCIA] " + responder_sobre_protocolo(montar_contexto(estado, "memoria")))


def main(numero):
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true", help="decisões simuladas, sem rede")
    parser.add_argument("--arquivo", type=Path, help="JSON da memória para o experimento 08")
    parser.add_argument("--fase", choices=("gravar", "recuperar"), default="recuperar")
    args = parser.parse_args()
    executar_cenario(numero, args.offline, args.arquivo, args.fase)
