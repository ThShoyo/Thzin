import os 
from dataclasses import dataclass

os.system("cls || clear ")

@dataclass
class Paciente: 
    # Atributos: são variáveis que pertencem  a classe.
    nome: str
    idade: int

    # Método: é uma função que pertence a uma classe.
    # Este método para exibir dados do pasciente.
    def exibir_dados(self):
        print(f"\tNome: {self.nome} \nIdade: {self.idade}\n\n")

# Criando uma lista.
lista_de_pacientes = []
QUANTIDADE_PACIENTES = 2

# Atribuindo dados dos paciente.
for i in range(QUANTIDADE_PACIENTES):
    paciente = Paciente(
                    nome=input("Digite o nome do paciente: "),
                    idade=int(input("Digite a idade do paciente: "))
                )
    lista_de_pacientes.append(paciente)
    print()

# Salvando em um aqeuivo com .txt
nome_arquivo = "Dados_pacientes.txt"
with open(nome_arquivo, "a") as arquivo:
    for paciente in lista_de_pacientes:
        arquivo.write(f"{paciente.nome}, {paciente.idade}\n")

print("Dados salvos com sucesso!")


# O "w" apaga pos escrever novamente, ja o "a" acomula.

# Exibindo dados dos pacientes.
print("\nExibindo dados dos pacientes: ")
for paciente in lista_de_pacientes:
    paciente.exibir_daados()