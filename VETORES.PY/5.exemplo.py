import os 
os.system("cls || clear")

lista_numeros = []
QUANTIDADES_NUMEROS = 6

def pares_impares(lista):
    pares = 0 
    impares = 0 
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

print("=Solicitando números =")
for i in range(QUANTIDADES_NUMEROS):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista_numeros.append(numero)

    pares, impares = pares_impares(lista_numeros)

print("\nMostrando números")
# Usando forEach numerando os eementos da lista.
# Iniciando contagem com a variavel i, começando com o número 1.
for i, numero in enumerate(lista_numeros, 1):
    print(f"{i}º número: {numero}")

print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")