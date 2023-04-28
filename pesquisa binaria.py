

#valor = input('informe o numero de busca binaria:')

"""
percore uma lista esquerda e direita As variáveis esquerda e
direita são inicializadas com os índices do início e fim do array
"""
def busca_binaria(array, valor_procurado):
    inicio = 0
    # len usada para retornar o comprimento n elementos
    fim = len(array) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if array[meio] == valor_procurado:
            return meio
        elif array[meio] < valor_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    return -1


# Exemplo de uso:
array = []
n = int(input("Digite o número de elementos do array: "))


# recebe a entrada de dados ref a tamanho da lista
for i in range(n):
    elemento = int(input(f"Digite o elemento {i + 1}: "))
    #é usado para adicionar um elemento ao final de uma lista
    array.append(elemento)

#busca
valor_procurado = int(input("Digite o valor que deseja procurar: "))
indice = busca_binaria(array, valor_procurado)

#validacao


if indice != -1:
    print(f"O valor {valor_procurado} foi encontrado no índice {indice}.")
else:
    print(f"O valor {valor_procurado} não foi encontrado no array.")


