import os 
from dataclasses import dataclass

os.system("cls || clear ")

@dataclass
class Pessoas: 
    nome: str
    data_de_nascimento: int
    RG: str
    CPF: str

    def exibir_dados(self):
        print(f"\tNome: {self.nome} \ndata de nascimento: {self.data_de_nascimento} \nRG: {self.RG} \nCPF: {self.CPF}\n\n")
   
lista_de_pessoas = []
QUANTIDADE_PESSOAS = 5

print("= Solicitando dados =")
for i in range(QUANTIDADE_PESSOAS):
    pessoas = Pessoas(
                    nome=input("Digite o nome do paciente: "),
                    data_de_nascimento=int(input("Digite a data de nascimento do paciente: ")),
                    RG=input("Digite o RG do paciente: "),
                    CPF=input("Digite o CPF do paciente: ")
                )
    lista_de_pessoas.append(pessoas)
    print()

print("n= Salvando dados =")
nome_arquivo = "Funcionarios.txt"
with open(nome_arquivo, "a") as arquivo:
    for pessoas in lista_de_pessoas:
        arquivo.write(f"Título: {pessoas.nome}, {pessoas.data_de_nascimento}, {pessoas.RG}, {pessoas.CPF}\n")
      
print("\n= Dados salvos com sucesso = ")

print("\n= Exibindo dados do arquivo =")

nome_arquivo = "Funcionarios.txt"
with open(nome_arquivo, "a") as arquivo:
    for pessoas in lista_de_pessoas:
        arquivo.write(f"Título: {pessoas.nome}, {pessoas.data_de_nascimento}, {pessoas.RG}, {pessoas.CPF}\n")
      
print("\n= Dados salvos com sucesso = ")

print("\n= Exibindo dados do arquivo =")

try: 
    with open(nome_arquivo, "r" , encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
              print(linha.strip())
except FileNotFoundError:
    print("Arquivo não encontrado.")
 