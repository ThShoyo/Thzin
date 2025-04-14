import os 
os.system("cls || clear")

def calcular_media(lista):
    return sum(lista_notas) / QUANTIDADE_NOTAS

def verificar_resultado(media):
    if media >= 7:
        resultado = "Aprovado"
    elif media <= 5:
        resultado = "Recuperação"
    else: 
        resultado = "Reprovado"
    return resultado

lista_notas = []
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite uma nota: "))
    lista_notas.append(nota)

media = calcular_media(lista_notas)
resultado = verificar_resultado(media)

print()
for nota in lista_notas: 
    print(nota)

print(f"Média: {media: .2f} ")
print(f"Resultado: {resultado}")