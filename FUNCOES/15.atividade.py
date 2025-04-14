import os
os.system("cls || clear")

soam = 0 

def calcular(soma):
    return soma / 2 

for  i in  range(2):
    nota = float(input("Digite uma nota: "))
    soma += nota

media =  calcular(soma)

print(f"Média: (media)")