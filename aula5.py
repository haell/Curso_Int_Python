# Função reduce
from functools import reduce
def soma(x, y):
    return x + y

lista = [1, 2, 3, 4, 5, 6]

soma = reduce(soma, lista) # Soma todos os elementos dentro de uma lista.

print(soma)

