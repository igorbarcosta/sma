from casos import buscar_caso


caso = buscar_caso("projetor")

print(f"PESSOA: {caso['mensagem_inicial']}")
print(
    "RESPOSTA: Entendo que há um problema com o projetor. Informe mais detalhes para que eu possa ajudar."
)
print("\nEsta resposta parece útil, mas não declara objetivo, estado, próxima decisão nem parada.")
