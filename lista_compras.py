# lista_compras.py

lista = []

while True:

    print("\n1-Adicionar")
    print("2-Pesquisar")
    print("3-Remover")
    print("4-Alterar")
    print("5-Listar")
    print("6-Sair")

    op = input("Opção: ")

    if op == "1":

        while True:
            produto = input("Produto: ").lower()

            if produto == "sair":
                break

            lista.append(produto)

    elif op == "2":

        produto = input("Pesquisar: ").lower()

        if produto in lista:
            print("Produto encontrado")
        else:
            print("Produto não encontrado")

    elif op == "3":

        produto = input("Remover: ").lower()

        if produto in lista:
            lista.remove(produto)
            print("Produto encontrado")
        else:
            print("Produto não encontrado")

    elif op == "4":

        produto = input("Produto: ").lower()

        if produto in lista:

            novo = input("Novo produto: ").lower()

            i = lista.index(produto)
            lista[i] = novo

            print("Produto alterado com sucesso")

        else:
            print("Produto não encontrado")

    elif op == "5":

        if lista:
            print(lista)
        else:
            print("Lista vazia")

    elif op == "6":

        print("Programa encerrado com sucesso!")
        break