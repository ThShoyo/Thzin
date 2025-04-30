import os 
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Endereco:
    logradouro: str
    numero: str 
    cidade: str

@dataclass
class Pessoa: 
    nome: str
    email: str
    endereco: Endereco # Classe endeço.

    def exibir_dados(self):
        print(f"\tNome: {self.nome} \n"
              f"\tEmail: {self.email} \n"
              f"\tLogradouro: {self.endereco.logradouro} \n"
              f"\tNúmero: {self.endereco.numero} \n"
              f"\tCidade: {self.endereco.cidade}")

nome = input("Digiter seu nome ")
email = input("Digite seu email ")
logradouro = input("Digite seu endereço ")
numero = input("Digite o número da sua residência ")
cidade = input("Digite o nome da cidade ")

endereco1 = Endereco(logradouro, numero, cidade)
pessoa1 = Pessoa(nome, email, endereco1)

print("\nDados da pessoas: ")
pessoa1.exibir_dados()
