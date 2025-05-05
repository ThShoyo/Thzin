import os
from dataclasses import dataclass

os.system("cls || clear ")

@dataclass
class Autor:
    nome: str
    bibliografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

    def exibir_detalhes(self):
        print(f'Título: {self.titulo} \nAno: {self.ano} \nAutor: {self.autor.nome}')

lista_de_livros = []

print("= Solicitando dados para o usário =")

livro = Livro(
        titulo=input("Digite o título do livro: "),
        ano=int(input("Digite o ano de publicação: ")),
        autor=Autor(
            nome=input("Digite o nome do autor: "),
            bibliografia=input("Digite as informações mde  bibliografia do autor: ")
        )
    )
lista_de_livros.append(livro)

print("n= Salvando dados =")
nome_arquivo = "dados_livros.txt"
with open(nome_arquivo, "w") as arquivo:
    for livro in lista_de_livros:
        arquivo.write(f"Título: {livro.titulo}, {livro.ano}, {livro.autor.nome}")
      
print("\n= Dados salvos com sucesso = ")

# Exibindo dados do arquivo txt.
print("\n= Exibindo dados do arquivo =")

try: 
    with open(nome_arquivo, "r" , encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
              print(linha.strip())
except FileNotFoundError:
    print("Arquivo não encontrado.")