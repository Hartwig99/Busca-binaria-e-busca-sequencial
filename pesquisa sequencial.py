Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def pesquisa_sequencial(lista, elemento):
...     for i in range(len(lista)):
...         if lista[i] == elemento:
...             return i  # Retorna o índice do elemento se encontrado
...     return -1  # Retorna -1 se o elemento não for encontrado
... 
... # Inserção dos dados
... lista = []
... n = int(input("Digite o número de elementos na lista: "))
... 
... for i in range(n):
...     elemento = int(input(f"Digite o elemento {i+1}: "))
...     lista.append(elemento)
... 
... elemento_pesquisa = int(input("Digite o elemento a ser pesquisado: "))
... 
... # Pesquisa sequencial
... indice = pesquisa_sequencial(lista, elemento_pesquisa)
... 
... if indice != -1:
...     print(f"O elemento {elemento_pesquisa} foi encontrado no índice {indice}.")
... else:
...     print(f"O elemento {elemento_pesquisa} não foi encontrado na lista.")
