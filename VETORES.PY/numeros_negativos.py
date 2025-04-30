import os
os.system("cls || clear")

lista_numeros = []
QUANTIDADE_NUMEROS = 5 
quantidade_negativos = 0 
soma_positivos = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

for numero in lista_numeros:
    if numero < 0:
        quantidade_negativos += 1
    else:
        soma_positivos += numero

print(f"\nQuantidade de números negativos: {quantidade_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")