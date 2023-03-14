import math

medida1 = input("Informe a medida da hipotenusa (ou deixe em branco se não souber): ")
medida2 = input("Informe a medida do cateto adjacente (ou deixe em branco se não souber): ")
medida3 = input("Informe a medida do cateto oposto (ou deixe em branco se não souber): ")

if medida1 == "" and medida2 != "" and medida3 != "":
    medida1 = math.sqrt(int(medida2)**2 + int(medida3)**2)
    if int(medida3) >= int(medida1):
        print("Não é possível formar um triângulo retângulo com as medidas informadas.")
        exit()
elif medida2 == "" and medida1 != "" and medida3 != "":
    medida3 = math.sqrt(int(medida1)**2 - int(medida2)**2)
    if int(medida3) >= int(medida1):
        print("Não é possível formar um triângulo retângulo com as medidas informadas.")
        exit()
elif medida3 == "" and medida1 != "" and medida2 != "":
    medida3 = math.sqrt(int(medida1)**2 - int(medida2)**2)
    if int(medida3) >= int(medida1):
        print("Não é possível formar um triângulo retângulo com as medidas informadas.")
        exit()

altura = int(medida3)
largura = int(medida2)

for i in range(altura):
    for j in range(largura):
        if j == 0 or i == altura-1 or i == altura-1-(j-1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
