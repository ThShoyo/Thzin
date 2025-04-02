import os 

# Função sem retorno 
def logo_senai():
    os.system("cls || clear")
    print("==SENAI==")


logo_senai() # Chamando função 
nome = input("Digite seu nome: ")

logo_senai() #Chamando função 
idade = int(input("Digite sua idade: "))

logo_senai() # Chamaando função 
print(f"Nome: {nome}") 
print(f"Idade: {idade}")