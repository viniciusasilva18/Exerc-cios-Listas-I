# Exercício 3 — Lista de tarefas

tarefas = []

while True:
    tarefa = input("Digite uma tarefa (ou 'fim' para encerrar): ")

    if tarefa.lower() == "fim":
        break

    tarefas.append(tarefa)

print("\nLista de tarefas:")
for item in tarefas:
    print("-", item)