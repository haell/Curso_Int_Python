# Função map

def dobro(x):
    return x*2

valor = [1, 2, 3, 4, 5]

# print(dobro(valor)) # Dessa forma faz apenas dobrar a lista.

# print(map(dobro, valor)) # Dessa forma ele retorna um objeto do tipo MAP.

valorDobrado =  map(dobro, valor)

# for v in valorDobrado:  # laço para imprimir cada elemento.
#     print(v)

valor_dobrado = list(valorDobrado) # Modo correto, atribuindo os valores dobrados a uma lista.
print(valor_dobrado)
