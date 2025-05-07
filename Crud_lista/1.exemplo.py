import os 
import time

os.system ("cls || clear ")

# Lista de nomes. 
lista_de_nomes = []

# Funçao para verificar se a lista está vazia>
def verificar_lista_vazia(lista_de_nomes):
    if not(lista_de_nomes):
        return True
    return False
    
# Função para adicionar.
def adicionar_nome(lista_nomes):
    nome = input("Digite o nome que deseja adicionar: ")
    lista_nomes.append(nome)
    print(f"\n{nome} adicionado com sucesso!")   

# Função para mostrar os nomes da lista.
def listar_nomes(lista_nomes):
    # Verificar lista vazia.
    if verificar_lista_vazia(lista_nomes):
        print("\nA lista está vazia!")
        return
    
    print("\n -Lista de nomes -")
    for nome  in lista_nomes:
        print(f"- {nome}")

def excluir_nomes(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print("\nA lista está vazia!")
        return
    
    listar_nomes(lista_nomes)
    nome_remover = input("Digite o nome que deseja remover: ")
    
    if nome_remover in lista_nomes:
        lista_nomes.remove(nome_remover)
        print(f"\n{nome_remover} foi removido com sucesso!")
    else:
        print(f"\n{nome_remover} não encontrado na lista.")

# Função para atualizar.
def atualizar_nome(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print("\nA lista está vazia!")
        return
    
    listar_nomes(lista_nomes)
    nome_antigo = input("Digite o nome que deseja atualizar: ")
    if nome_antigo in lista_nomes:
        novo_nome = input("Digite o novo nome: ")
        indice = lista_nomes.index(nome_antigo)
        lista_nomes[indice] = novo_nome
        print(f"\n{nome_antigo} foi atualizado para {novo_nome}.")
    else:
        print(f"\nO nome {nome_antigo} não encontrado na lista.")

# Mostrar menu.

while True:
    print("""
- Gerenciadosr de nomes- 
1 - Adicionar
2 - Listar nomes
3 - Atualizar
4 - Remover
5 - Sair     
""")
    opcao = int(input("Digite uma opções acima: "))
    
    match opcao:
         case 1: 
            adicionar_nome(lista_de_nomes)
         case 2:
            listar_nomes(lista_de_nomes)
         case 3:
                ...
         case 4:
            ...
         case 5: 
            print("Saindo do programa...")
            break
    time.sleep(4)
    os.system("cls || clear")