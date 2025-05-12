import os
from dataclasses import dataclass
import time

os.system("cls || clear")

@dataclass

class Funcionario:
    nome: str
    data_nascimento: int
    cpf: str
    funcao: str

    def exibir(self):
        print(f"\nNome: {self.nome}\nData de Nascimento: {self.data_nascimento}\nCPF: {self.cpf}\nFunção: {self.funcao}")

print(f"\t= Solicitação de Dados =")
funcionario = Funcionario(
nome=input("Digite o nome do funcionário: "),
data_nascimento=input("Digite a data de nascimento do funcionário: "),
cpf=input("Digite o CPF do funcionário: "),
funcao=input("Digite a função do funcionário: ")
        )

def  limpar():
    os.system("cls || clear")

lista_nomes = []

def verificar_lista_vazia(lista_nomes):
    if not lista_nomes: # Se a lista NÃO tem conteúdo, retona o valor 'VERDADEIRO'
        print("\nA lista está vazia.")
        return True
    return False # Se a lista possui algum conteúdo.

def adicionar_nome(lista_nomes):
    nome = input("Digite o nome que deseja adicionar: ")
    lista_nomes.append(nome)
    print(f"\n{nome} adicionado com sucesso.")

def listar_nomes(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        return  
    
    print("\n - Lista de nomes - ")
    for nome in lista_nomes:
        print(f"- {nome}")

def excluir_nome(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print("\nA lista está vazia.")
        return

    listar_nomes(lista_nomes)

    nome_remover = input("Digite o nome que deseja remover: ")
    if nome_remover in lista_nomes: # Percorre a lista para encontrar o nome informado.
        lista_nomes.remove(nome_remover)
        print(f"\n{nome_remover} removido com sucesso.")
    else:
        print(f"\nO nome {nome_remover} não foi encontrado.")

def atualizar_nome(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print
        return

    listar_nomes(lista_nomes)
    nome_antigo = input("Digite o nome que deseja atualizar: ")
    novo_nome = input(f"Digite o novo nome para {nome_antigo}: ")
    if nome_antigo in lista_nomes: 
        indice = lista_nomes.index(nome_antigo) 
        lista_nomes[indice] = novo_nome 
        limpar()
        print(f"O nome {nome_antigo} foi atualizado para {novo_nome}.")
    else:
        print(f"\nO nome {nome_antigo} não foi encontrado.")

while True:
        print("""
- Gerenciador de nomes -
1- Adicionar
2- Listar nomes
3- Atualizar
4- Remover
5- Sair
""")
        opcao = input("Digite a opção desejada: ")

        match opcao:
            case 1:
                adicionar_nome(lista_nomes)
            case 2:
                listar_nomes(lista_nomes)
            case 3:
                atualizar_nome(lista_nomes)
            case 4:
                excluir_nome(lista_nomes)
            case 5:
                os.system("cls || clear")
                print(f"\nPrograma Finalizado.")
                break
            case _:
                print("Opção inválida.")
        for funcionario in lista_nomes:
            funcionario.exibir

        if opcao != 1:
            time.sleep(3.5)
            os.system("cls || clear") 
                   