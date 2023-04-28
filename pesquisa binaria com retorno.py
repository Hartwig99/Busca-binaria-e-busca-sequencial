def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == item:
            return meio

        if lista[meio] > item:
            fim = meio - 1
        else:
            inicio = meio + 1

    while True:
        print("O número não foi encontrado na lista. Tente novamente.")
        novo_item = int(input("Digite um novo número para pesquisar: "))
        posicao = busca_binaria(lista, novo_item)
        if posicao is not None:
            return posicao


lista = input("Digite uma lista de números separados por espaço: ").split()
lista = [int(x) for x in lista]

item = int(input("Digite o número para pesquisar: "))
posicao = busca_binaria(lista, item)

print("O número foi encontrado na posição:", posicao)
