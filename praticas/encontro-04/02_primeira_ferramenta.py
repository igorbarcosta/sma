from ambiente import criar_ambiente, retrato
from ferramentas import abrir_chamado


ambiente = criar_ambiente()
print(f"[AMBIENTE ANTES]\n{retrato(ambiente)}")
print("\n[FERRAMENTA]\nabrir_chamado(local='Lab 4', problema='projetor não funciona')")
resultado = abrir_chamado(ambiente, "Lab 4", "projetor não funciona")
print(f"\n[RESULTADO DA FERRAMENTA]\n{resultado}")
print(f"\n[AMBIENTE DEPOIS]\n{retrato(ambiente)}")
print("\nQuem modificou o ambiente foi a ferramenta executada pelo programa.")
