import os
os.system("cls || clear")

contador = 0 
continua = 'S'

while continua == 'S':
    #comandos a serem repetidos
    print("Repentindo...")

contador += 1
continua = input("Tecle 'S' se deseja continuar: ").strip().lower()
 
if contador == 0:
    print("O bloco não foi repetido.")
else: 
    print(f"O bloco foi rpetido {contador} vezes")