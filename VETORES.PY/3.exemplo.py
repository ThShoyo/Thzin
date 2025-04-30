import os 
os.system("cls || clear")
import time

lista_numeros = []
QUANTINDADE_NUMEROS = 5

print("=Solicitando números =")
for i in range(QUANTINDADE_NUMEROS):
    numero = int(input(f"Digite o {i +1} número: "))
    lista_numeros.append(numero)

# Verificando maior e menor números em uma lista.
# As funções max() e min percorrem o vetor e mosteram o maior e 
# o menor número respectivamente.
maior = max(lista_numeros)
menos = min(lista_numeros)

print("\nMostrando números")
# Usando ForEach numerando os elementos da lista. 
# Iniciando contagem com a variavel i, començando com o número 1.
for i, numero in enumerate(lista_numeros, start=1):
    print(f"{i}º {numero}")
    time.sleep(5)

print(f"\nMaior número: {maior}")
print(f"Menor número: {menos}")