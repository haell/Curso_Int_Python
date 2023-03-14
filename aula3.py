# Para obter o elemento e ao mesmo tempo o indice do elemento.

lista = ["bola", "cachorro", "leite"]

for i in range(len(lista)):
    print(i, lista[i])

# Utilizando a função enumerate
    if i == 2:
        print("-" * 20)
for i, nome in enumerate(lista):
    print(i, nome)
