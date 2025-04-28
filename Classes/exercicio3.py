import os 
from dataclasses import dataclass

os.system ("cls || clear")



class Pessoa(): 
    nome : str
    email: int
    telefone: float
    endereco: float

    def exebindo_dados(self): 
        print("\nExibindo dados: ")
        print(f"Nome: {self.nome}, e-mail: {self.email}, telefone:{self.telefone},endereço: {self.endereco}")

print("Solicitando dados: ")
nome = input("Digite seu nome:")
email = input("Digite seu e-mail :")
telefone = input("Digite seu telefone: ")
endereco = input("Digite seu endereço: ")

pessoa1 = Pessoa(nome, email, telefone, endereco)
pessoa1.exibindo_dados()
