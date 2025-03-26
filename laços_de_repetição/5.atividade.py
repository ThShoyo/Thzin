import os

os.system ("cls || clear")

media_geral = 0 
contador = 0
soma = 0 
pares = 0 
impares = 0 
while True:
    numero = int(input(f"Digite o {contador + 1}º número: "))
    if numero == 0: 
        break
    elif numero% 2 == 0:
        quantidade_pares += 1
        soma_pares = numero
    else:
       quantidade_impares += 1
        
    soma_geral += numero
    contador += 1

    media_pares = soma_pares / quantidade_pares
    media_geral += soma_geral / contador
    print (f"Quantidades de pares: {quantidade_pares}")
    print (f"quantidade de ímpares: {quantidade_impares}")
    print (f"Média pares: {media_pares:}")
    print (f"Média geral: {media_geral}")
    