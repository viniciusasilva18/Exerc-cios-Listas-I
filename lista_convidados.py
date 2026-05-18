# Exercício 1 — Lista de convidados

convidados = []

for i in range(5):
    nome = input(f"Digite o nome do {i+1}º convidado: ")
    convidados.append(nome)

print("\nLista de convidados:")
for convidado in convidados:
    print(convidado)

print(f"\nQuantidade de convidados: {len(convidados)}")