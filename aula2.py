x = [1, 2, 3, 4, 5, 6]
y = []
for i in x:
    y.append(i**2)
print("Utilizando laço FOR\n", x, "\n", y)

# Utilizando comprehension #

z = [i**2 for i in x]
print(z)


# imprimindo apenas os número IMPARES utilizando comprehension #

w = [i for i in x if i%2==1]
print(w)

# imprimindo apenas os número PARES utilizando comprehension #

K = [i for i in x if i%2==0]
print(K)
