import os 
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    data_de_admissao: str
    matricula: str
    endereco: str
    
@dataclass
class Cliente:
    nome: str
    data_de_nascimento: str
    endereco: str

    def exibir_detalhes(self):
        print(f'Nome: {self.nome} \nData de Admissão: {self.data_de_admissao} \nMatrícula: {self.matricula} \nEndereço: {self.endereco}')

lista_de_funcionarios = []
QUANTIDADE_FUNCIONARIOS = 3

print("= Solicitando dados =")

for i in range(QUANTIDADE_FUNCIONARIOS):
    funcionarios = Funcionario(
                nome=input(f"\nDigite o nome do funcionário: "),
                data_de_admissao=input("Digite a data de admissão: "),
                matricula=input("Digite a matrícula: "),
                endereco=input("Digite o endereço: ")
            )
    lista_de_funcionarios.append(funcionarios)

print(" Salvando dados ")

lista_de_clientes = []
QUANTIDADE_CLIENTES = 3

for i in range(QUANTIDADE_CLIENTES):
    clientes = Cliente(
                    nome=input("Digite o nome do cliente: "),
                    data_de_nascimento=input("Digite a data de nascimento do cliente: "),
                    endereco=input("Digite o endereço do cliente: ")
                )
    lista_de_clientes.append(clientes)
    print()

print("\n Salvando dados ")

nome_arquivo = "Funcionarios.txt"
with open(nome_arquivo, "a") as arquivo:
    for funcionarios in lista_de_funcionarios:
        arquivo.write(f"Nome: {funcionarios.nome}, {funcionarios.data_de_admissao}, {funcionarios.matricula}, {funcionarios.endereco}\n")
      
print("\n= Dados salvos com sucesso = ")


print("\n= Exibindo dados do arquivo =")

nome_arquivo = "Clientes.txt"
with open(nome_arquivo, "a") as arquivo:
    for clientes in lista_de_clientes:
        arquivo.write(f"Título: {clientes.nome}, {clientes.data_de_nascimento}, {clientes.endereco}\n")
      
print("\n= Dados salvos com sucesso = ")

print("\n= Exibindo dados do arquivo =")

try: 
    with open(nome_arquivo, "r" , encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
              print(linha.strip())
except FileNotFoundError:
    print("Arquivo não encontrado.")