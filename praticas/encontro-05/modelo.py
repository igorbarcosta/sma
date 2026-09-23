"""Mesmo prompt, mesmas ferramentas e mesmo decisor em todos os cenários."""

import json
import os
import tomllib
from pathlib import Path


PROMPT_BASE = (
    "Você é o decisor do CampusBot. Objetivo: verificar se já há chamado para o projetor "
    "do local; se não houver, abrir um. Use apenas o contexto recebido. "
    "Ferramentas: consultar_chamados(local), abrir_chamado(local, problema). "
    "Se a consulta mostrar chamado, responda sem duplicar. Se não mostrar, abra. "
    "Se não houver resultado de consulta, consulte. Após abrir, responda com o protocolo. "
    "Devolva JSON com tipo=responder e mensagem, ou tipo=usar_ferramenta, ferramenta e argumentos."
)


def _simular(contexto):
    abertura = contexto.get("ultima_abertura")
    consulta = contexto.get("ultima_consulta")
    if abertura and abertura.get("ok"):
        return {"tipo": "responder", "mensagem": f"O chamado {abertura['protocolo']} foi aberto."}
    if consulta is None:
        return {"tipo": "usar_ferramenta", "ferramenta": "consultar_chamados", "argumentos": {"local": contexto["local"]}}
    if consulta["chamados"]:
        return {"tipo": "responder", "mensagem": f"Já existe o chamado {consulta['chamados'][0]['protocolo']}."}
    return {"tipo": "usar_ferramenta", "ferramenta": "abrir_chamado", "argumentos": {"local": contexto["local"], "problema": contexto["problema"]}}


def decidir(contexto, offline):
    if offline:
        decisao = _simular(contexto)
    else:
        chave = os.environ.get("GEMINI_API_KEY")
        if not chave:
            raise RuntimeError("Defina GEMINI_API_KEY ou execute com --offline.")
        from google import genai
        raiz = Path(__file__).resolve().parents[2]
        with (raiz / "config/llm.toml").open("rb") as arquivo:
            config = tomllib.load(arquivo)
        if config.get("provider") != "gemini":
            raise ValueError("Esta prática espera Gemini em config/llm.toml.")
        cliente = genai.Client(api_key=chave)
        try:
            resposta = cliente.models.generate_content(
                model=config["model"],
                contents=PROMPT_BASE + "\nContexto: " + json.dumps(contexto, ensure_ascii=False),
                config={"response_mime_type": "application/json", "temperature": 0},
            )
        finally:
            cliente.close()
        decisao = json.loads(resposta.text)
    if decisao.get("tipo") == "responder" and isinstance(decisao.get("mensagem"), str):
        return decisao
    if decisao.get("tipo") == "usar_ferramenta" and decisao.get("ferramenta") in {"consultar_chamados", "abrir_chamado"}:
        args = decisao.get("argumentos", {})
        exigidos = ("local", "problema") if decisao["ferramenta"] == "abrir_chamado" else ("local",)
        if all(isinstance(args.get(c), str) and args[c] for c in exigidos):
            return decisao
    raise ValueError(f"Decisão fora do contrato: {decisao}")


def responder_sobre_protocolo(contexto):
    """Uma pergunta simples evidencia a ausência ou presença da lembrança."""
    lembranca = contexto.get("memoria")
    if lembranca is None:
        return "Não sei o protocolo nesta nova execução."
    return f"O protocolo lembrado é {lembranca['protocolo']}; status lembrado: {lembranca['status']}."
