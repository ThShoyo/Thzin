import os 
os.system("cls || clear")

#Criando uma lista.
lista_notas = []
QUANTIDADE_NOTAS = 3

# Adicionando 3 notas em uma lista.]
for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite uma nota: "))
    lista_notas.append(nota)

# Soma
media = sum(lista_notas) / QUANTIDADE_NOTAS

# Exibindo todos os valores em uma lista.
print()
for nota in lista_notas:    #ForEach
    print(nota) 

print(f"Média: {media: .2f} ")