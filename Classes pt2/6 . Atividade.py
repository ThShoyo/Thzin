import os 
from dataclasses import dataclass

os.system("cls || clear ")

@dataclass
class Pessoas: 
    # Atributos: são variáveis que pertencem  a classe.
    nome: str
    data_de_nascimento: int
    RG: str
    CPF: str

    # Método: é uma função que pertence a uma classe.
    # Este método para exibir dados do pasciente.
    def exibir_dados(self):
        print(f"\tNome: {self.nome} \ndata de nascimento: {self.data_de_nascimento} \nRG: {self.RG} \nCPF: {self.CPF}\n\n")
   
# Criando uma lista.
lista_de_pessoas = []
QUANTIDADE_PESSOAS = 5

# Atribuindo dados dos paciente.
for i in range(QUANTIDADE_PESSOAS):
    pessoas = Pessoas(
                    nome=input("Digite o nome do paciente: "),
                    data_de_nascimento=int(input("Digite a data de nascimento do paciente: ")),
                    RG=input("Digite o RG do paciente: "),
                    CPF=input("Digite o CPF do paciente: ")
                )
    lista_de_pessoas.append(pessoas)
    print()

nome_arquivo = "Funcionarios.txt"
with open(nome_arquivo, "a") as arquivo:
    for livros in lista_de_pessoas:
        arquivo.write(f"{livros.nome}, {livros.data_de_nascimento}, {livros.RG}, {livros.CPF}\n")

print("Dados salvos com sucesso!")

# Exibindo dados dos pacientes.
print("\nExibindo dados dos pacientes: ")
for paciente in lista_de_pessoas:
    paciente.exibir_dados()