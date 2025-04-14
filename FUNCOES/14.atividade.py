import os 
os.system ("cls || clear")


def calcular(idade):
    resultado = 2025 - idade

    return resultado

ano_nascimento = int(input("Digite o ano de nascimento: "))

idade  = calcular(ano_nascimento)

print(f"Idade: {idade}")