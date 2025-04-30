import os 
from dataclasses import dataclass

os.system("class || clear ")

@dataclass 
class Paciente:
    nome: str 
    idade: int 
    peso: float
    altura: float




def exibir_dados(self):
    print(f"Nome: {self.nome} \nIdade: {self.idade} \nPeso: {self.peso} \nAltura: {self.altura}")


lista_de_pessoas = []
QUANTIDADE_PACIENTES = 4

for i in range(QUANTIDADE_PACIENTES): 
    paciente = Paciente(  
                    nome = input("Digite seu nome: "),
                    idade = int(input("Digite sua idade: ")),
                    peso = float(input("Digite seu peso: ")),
                    altura = float(input("Digite sua altura: "))
                
                )
    lista_de_pessoas.append(paciente)            
    print()


print("\nExibindo dados do usuário.")
for paciente in lista_de_pessoas:
    paciente.exibir_dados()