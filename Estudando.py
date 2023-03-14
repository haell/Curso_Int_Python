import random

meuDicionario = {
    'item1':'primeiro item.',
    'item2':'segundo item.',
    'item3':'terceiro item.'
}

print(meuDicionario['item3'], meuDicionario['item2'], meuDicionario['item1'])

# random.seed(x) para forçar cair sempre o mesmo número.
numero = random.randint(0, 10)
print(numero)

listinha = [17, 21, 37, 56, 1, 7]
numero2 = random.choice(listinha)
print(numero2)

a = 2
b = 0

try:
    print(a/b)
except:
    print("Não é permitido dividir por 0")
print(
    "Após o tratamento do erro, a execução continua."
)

texto = input('Digite o texto')
numeroInteiro = int(input("Digite um número inteiro: "))
numeroDecimal = float(input("Digite um número decimal"))

