import math

print("Para resolver uma equação do 2° Grau, digite os termos na sequência.")
print(" >>> ax²-bx-c=0 <<< ")
print("| Primeiro termo = 'ax²' | Segundo termo = 'bx' | Terceiro termo = c\n")

while True:
    a = float(input("Digite o termo a: "))
    c = float(input("Digite o termo c: "))

    # Loop para evitar que o usuário digite um valor inválido para b
    while True:
        b = float(input("Digite o termo b: "))
        delta = b ** 2 - 4 * a * c
        if delta >= 0:
            break
        else:
            print("O valor de delta é negativo. Digite um novo valor para b.")

    print("\nCriando a equação...")
    print(f"Termo 'a': {a}x²")
    print(f"Termo 'b': {b}")
    print(f"Termo 'c': {c}\n")
    print(f"Sua equação: {a}x²+({b})+{c}=0\n")

    resposta = input("Digite 'R' para resolver ou 'S' para sair: ").lower()
    if resposta == "s":
        break
    elif resposta == "r":
        print("\nDescobrindo valor de Delta: (▲ = b² - 4ac)...\n")
        print(f"▲ = ({b})²-4.{a}.{c}")
        print(f"▲ = {b**2}-4.{a}.{c}")
        print(f"▲ = {b**2-4*a*c}\n")

        if delta == 0:
            x = -b / (2 * a)
            print(f"Delta é igual a zero. A solução é única: x = {x}\n")
        else:
            print("Aplicando a fórmula de Bhaskara")
            print("X = -b ± √▲")
            print("-----------")
            print("     2a\n")
            print(f"X = -({b}) ± √({delta})")
            print(f"----------------")
            print(f"     2.({a})\n")

            raizDeDelta = math.sqrt(delta)
            x1 = (-b + raizDeDelta) / (2 * a)
            x2 = (-b - raizDeDelta) / (2 * a)

            print(f"As soluções são: x1 = {x1} e x2 = {x2}\n")
