# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.
calcular = True

while calcular:
    try:
        numero1 = int(input("Informe um número: "))
        numero2 = int(input("Informe outro número: "))
        operador = input("Digite um dos operadores (+, -, /, *): ")

        if operador == '+':
            resultado = numero1 + numero2
            print(f"{numero1} + {numero2} = {resultado}")
            calcular = False
        elif operador == '-':
            resultado = numero1 - numero2
            print(f"{numero1} - {numero2} = {resultado}")
            calcular = False
        elif operador == '/':
            resultado = numero1 / numero2
            print(f"{numero1} / {numero2} = {resultado}")
            calcular = False
        elif operador == '*':
            resultado = numero1 * numero2
            print(f"{numero1} * {numero2} = {resultado}")
            calcular = False
        else:
            print("Operador inválido. Tente novamente.")

    except ValueError:
        print("Os valores informados devem ser números inteiros. Tente novamente.")

### Resposta do professor ############################################################
n1 = int(input("Digite o primeiro número: "))
sinal = input("Digite o sinal: ")
n2 = int(input("Digite o segundo número: "))

if sinal == "+":
    op = n1 + n2

elif sinal == "-":
    op = n1 - n2

elif sinal == "/":
    op = n1 + n2

elif sinal == "*":
    op = n1 * n2

else:
    print("Sinal inválido.")

print(op)
