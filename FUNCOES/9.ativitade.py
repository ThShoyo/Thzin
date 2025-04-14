import os 
os.system("cls || clear")

def diferenca(numero):
    if numero < 0:
        print("Número negativo.")
    elif numero == 0:
        print(f"NÚMERO NEUTRO IDENTIFICADO ({numero})")
    else:
        print("Número positivo.")

print("= POSITIVO OU NEGATIVO =")
numero = int(input("Digite um número: "))
diferenca(numero)