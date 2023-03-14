import sys
import time
import math

print("Para resolver uma equação do 2° Grau, digite os termos na sequência.")
print(">>> ax²-bx-c=0 <<< ")
print("| Primeiro termo = 'ax²' | Segundo termo = 'bx' | Terceiro termo = c")

# solicita os termos da equação
a = float(input("Digite o termo a: "))
b = float(input("Digite o termo b: "))
c = float(input("Digite o termo c: "))

# cria a equação
equacao = f"{a}x²{b:+}x{c:+}=0"

print(f"\nCriando a equação...\nTermo 'a': ", end="")
if a.is_integer():
    print(f"{int(a)}²")
else:
    print(f"{a}²")

print(f"Termo 'b': {b}")
print(f"Termo 'c': {c}")
print(f"Sua equação: {equacao}\n")

# Loop para calcular a equação
while True:
    # calcula delta
    delta = b ** 2 - 4 * a * c

    # verifica se delta é negativo
    if delta < 0:
        print(f"Delta é negativo: {delta}")
        # solicita um novo valor para o segundo termo
        novo_b = input("Digite um novo valor para o segundo termo (ou 'q' para sair): ")
        if novo_b.lower() == 'q':
            print("Programa encerrado.")
            break
        b = float(novo_b)
        # atualiza a equação
        equacao = f"{a}x²{b:+}x{c:+}=0"
        print(f"Sua nova equação: {equacao}\n")
    else:
        # delta é positivo ou igual a zero, a equação pode ser resolvida
        print(f"Delta = {delta}")
        # aplica a fórmula de Bhaskara
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"\nSoluções:\nx1 = {x1}\nx2 = {x2}")
        break
# Montando a equação do 2° Grau.

print("\nCriando a equação...")
time.sleep(2)
print('Termo "a": {a}² \nTermo "b": {b} \nTermo "c": {c}'. format(a=a, b=b, c=c))
time.sleep(2)
print("\nSua equação: {a}²+({b})+{c}=0\n". format(a=a, b=b, c=c))

# Opção de calcular o resultado da Equação ou encerrar o programa.

estarte = input("Digite 'R' para resolver ou 'S' para sair:  ").upper()
print("\n")

if (estarte == 'R') :   # Caso escolha o 'Resultado' ...  Descobrindo o valor de ▲ (Delta)
    print('Descobrindo valor de Delta: (▲ = b² - 4ac)...\n')
    time.sleep(2)
    print('▲ = ({b})²-4.{a}.{c}'. format(b=b, a=a, c=c))
    time.sleep(1)
    b1 = b**2
    print('▲ = {b} - 4.{a}.{c}'. format(b=b1, a=a, c=c))
    time.sleep(1)
    a1 = 4*a
    print('▲ = {b}-{a}.{c}'. format(b=b1, a=a1, c=c))
    time.sleep(1)
    c1 = a1 * c
    print('▲ = {b}-{c}'.format(b=b1, c=c1))
    time.sleep(1)
    delta1 = b1 - c1
    print('▲ = ', delta1)
    print('\n')
    time.sleep(3)

    # Utilizando o valor de ▲ (Delta) para resolver a equação do 2° Grau, com a fórmula de Bhaskara

    print('Aplicando a fórmula de Bhaskara\nX = -b ± √▲\n-----------\n     2a\n')
    time.sleep(4)
    print('X = -({b}) ± √({delta})\n----------------\n     2.({a})\n'. format(b=b, delta=delta1, a=a))
    time.sleep(3)
    bMultiplicado = (-1) * b
    raizDeDelta = math.sqrt(delta1)
    base = 2 * a
    print('X = {bMultiplicado} ± {raizDeDelta}\n------------\n     {base}\n'. format(bMultiplicado=bMultiplicado, raizDeDelta=raizDeDelta, base=base))
    time.sleep(2)
    print("Calculando os dois resultados: X' e X'' ")
    time.sleep(3)
    bMenosRaizDelta = bMultiplicado - raizDeDelta
    bMaisRaizDelta = bMultiplicado + raizDeDelta
    dvdPbasePositiva = bMaisRaizDelta / base
    dvdPbaseNegativa = bMenosRaizDelta / base

    # Calculando o resultado X' subitraindo.
    print("\nX' = {bMultiplicado} + {raizDeDelta}  =  {bMaisRaizDelta}\n------------     ---  =  {dvdPbasePositiva}\n     {base}            {base}". format(bMultiplicado=bMultiplicado, raizDeDelta=raizDeDelta, bMaisRaizDelta=bMaisRaizDelta, dvdPbasePositiva=dvdPbasePositiva, base=base))
    time.sleep(3)

    # Calculando o resultado X'' subitraindo.
    print("\nX'' = {bMultiplicado} - {raizDeDelta}  =  {bMenosRaizDelta}\n-------------     ---  =  {dvdPbaseNegativa}\n      {base}            {base}". format(bMultiplicado=bMultiplicado, raizDeDelta=raizDeDelta, bMenosRaizDelta=bMenosRaizDelta, dvdPbaseNegativa=dvdPbaseNegativa, base=base))

else:
    sys.exit()

### Resposta do professor ############################################################
from math import sqrt

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Delta negativo")
else:
    raiz_delta = sqrt(delta)
    x1 = (-b + raiz_delta) / 2 * a
    x2 = (-b - raiz_delta) / 2 * a

    print("As raízes são", x1, "e", x2)