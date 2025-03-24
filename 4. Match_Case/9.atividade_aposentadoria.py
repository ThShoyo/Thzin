import os
os.system ("clear || cls")



matricula = input("Digite sua matrícula: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
tempo_trab = int(input("Digite seu tempo de trabalho em anos: "))

# Processamento
idade = 2025 - ano_nascimento

if idade > 65 or tempo_trab >= 30:
    resultado = "Requerer aposentadoria!"
else: 
    resultado = "Não requerer aposentadoria!"

    print (f"\nMatricula: {matricula}")
    print (f"Idade: {idade}")
    print (f"Tempo de trabalho: {tempo_trab}")
    print (f"Resultado: {resultado}")