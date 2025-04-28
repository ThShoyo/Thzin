import os 
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Endereco:
    logradouro: str
    numero: str

@dataclass
class Pessoa :
    # Atributos da classes (variáveis que pertencem a uma classe ).
    nome: str 
    idade : int
    endereco : Endereco # Classe endereço.

    # Método da classe (função que pertence a uma classe).
    def exibir_dados(self):
        print (f"Nome: {self.nome}, Idade: {self.idade}, Logradouro: {self.endereco.logradouro}, Número: {self.endereco.numero}")

# Solicitando Dados
endereco1 = Endereco("Rua A", "33")
pessoa1 = Pessoa("Marta", 22, endereco1)

print("Dados das pessoas: ")
pessoa1.exibindo_dados()
