import os
os.system ("cls || clear")


QUANTIDADE_NOTAS = 3
SOMA = 0 

for i in  range(QUANTIDADE_NOTAS):
    while True:
        nota = float (input("Digite uma nota: " ))

        if nota < 0 or  nota > 10:
            print("Nota inválida. \nTente novamente...\n")
        else:
            soma += nota 
            break

media = soma / QUANTIDADE_NOTAS

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Recuperação"
    
print(f"\nMédia: {media}")
print(f"Resultado: {resultado}")