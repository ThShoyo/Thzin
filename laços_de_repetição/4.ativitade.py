import os

os.system ("cls || clear")

contador = 0 
soma = 0
while True:
    nota = float(input("Insira um valor: "))
    if nota < 0:
        soma += nota 
        contador += 1 
    else:
        break

media = soma / contador
print(f"\nSua média de números positivos: {media:.2f}")