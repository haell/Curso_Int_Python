# Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.

idade = int(input("Digite sua idade: "))

if (idade >= 18 and idade < 65) :
    print("Maior de idade!")
elif ( idade < 18):
    print("Menor de idade!")
else:
    print("Idoso!")

### Resposta do professor ############################################################
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")
elif idade < 18:
    print("Menor de idade")