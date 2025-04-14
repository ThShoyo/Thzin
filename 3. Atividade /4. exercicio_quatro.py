import os
os.system("cls || clear")





numero_um=float(input("Digite o primeiro número: "))
numero_dois=float(input("Digite o segunddo número"))

media = (numero_um + numero_dois) / 2
produto = numero_um * numero_dois

if numero_um > numero_dois:
    maior = numero_um
    menor = numero_dois
else: 
    maior = numero_dois 
    menor = numero_um

print(f"\nA média é: {media}") # Contrabarra + n serve para quebrar linha 
print(f"\nO produto é: {produto}") # Contrabarra + n serve para quebrar linha 
print(f"\nMaior: {maior}") # Contrabarra + n serve para quebrar linha 
print(f"\nMenor: {menor}") # Contrabarra + n serve para quebrar linha 