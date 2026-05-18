# Exercício 2 — Controle de preços

precos = []

for i in range(5):
    preco = float(input(f"Digite o {i+1}º preço: "))
    precos.append(preco)

print("\nLista de preços:", precos)
print("Maior preço:", max(precos))
print("Menor preço:", min(precos))