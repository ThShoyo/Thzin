import os 
import time

os.system("cls || clear")

numero = int(input("Digite um numero: "))

print("contagem regressiva")
for i in range(numero,0,-1):
    print(f"valor da variavel i : {i}") 
    print("...")
    time.sleep(1)
