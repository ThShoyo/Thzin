import os 
from dataclasses import dataclass

os.system("cls || clear")

#Definindo classes 
@dataclass
class Pessoa():
    nome: str
    idade: int
    peso: float
    altura: float

# Definindo valores.
# pessoa1 - Pessoa("Marta" , 33, 55.333, 1,69)0

print("Solicitando dados: ")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

pessoa1 = Pessoa(idade=idade, nome=nome, peso=peso, altura=altura)
pessoa2 = Pessoa(idade, nome, peso , altura)
