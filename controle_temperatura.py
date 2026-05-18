# Exercício 4 — Controle de temperaturas

celsius = []

while True:
    entrada = input("Digite a temperatura em Celsius (ou 'sair'): ")

    if entrada.lower() == "sair":
        break

    temperatura = float(entrada)
    celsius.append(temperatura)

fahrenheit = []

for temp in celsius:
    f = (temp * 9/5) + 32
    fahrenheit.append(f)

if len(celsius) > 0:
    media_celsius = sum(celsius) / len(celsius)
    media_fahrenheit = sum(fahrenheit) / len(fahrenheit)

    print("\nTemperaturas em Celsius:", celsius)
    print("Temperaturas em Fahrenheit:", fahrenheit)

    print(f"\nMédia Celsius: {media_celsius:.2f}")
    print(f"Média Fahrenheit: {media_fahrenheit:.2f}")
else:
    print("Nenhuma temperatura foi cadastrada.")