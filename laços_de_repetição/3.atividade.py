import os

os.system ("cls || clear")

contador = 0
soma = 0 

while True:
    for i in range (2):
        nota = int (input("Digite uma nota: "))
        resposta= ("Deseja inserir mais uma nota? \nDigite 'S' ou 'N' ") .upper()

        if resposta == 'N':
            break
