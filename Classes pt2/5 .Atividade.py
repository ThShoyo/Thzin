import os 
from dataclasses import dataclass

os.system(" cls || clear ")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preço: float

    def exibir_dados(self):
        print(f"\tNome: {self.nome} \n",
              f"\tAutor: {self.autor} \n",
              f"\tCategoria: {self.categoria} \n",
              f"\tPreço: {self.preço} \n"
              
              )

lista_de_livros = []
QUANTIDADE_LIVROS = 3

for i in range(QUANTIDADE_LIVROS):
    livros = Livro(
                    nome=input("Digite o nome do livro: "),
                    autor=input("Digite o nome do autor: "),
                    categoria=input("Digite a categoria: "),
                    preço=float(input("Digite o preço: "))
                )
    lista_de_livros.append(livros)
    print()           
        
nome_arquivo = "Catalogos_livros.txt"
with open(nome_arquivo, "a") as arquivo:
    for livros in lista_de_livros:
        arquivo.write(f"{livros.nome}, {livros.autor}, {livros.categoria}, {livros.preço}\n")

print("Dados salvos com sucesso!")
        
print("\nExibindo dados dos livros: ")
for livros in lista_de_livros:
    livros.exibir_dados()

   