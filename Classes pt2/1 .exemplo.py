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

# Atribuindo dados a classe paciente.
pacientel = Paciente(nome="Marta", idade=45)

# Exibindo dados do pasciente.
pacientel.exibir_dados()