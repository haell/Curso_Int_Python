# -*- contest: UTF-8 -*-
# Faça um programa que receba duas notas digitadas pelo usuário.
# Se a média das notas forem maior ou igual a seis, escreva aprovado, senão escreva reprovado.

nota1 = float(input("Digite 1° nota: "))
nota2 = float(input("Digite 2° nota: "))

try:
    media = (nota1 + nota2)/2
except:
    print("Digite apenas valores decimais separados por ponto.")

if (media >= 6):
    print("aprovado ", media)
else:
    print("reprovado ", media)


### Resposta do professor ############################################################
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")