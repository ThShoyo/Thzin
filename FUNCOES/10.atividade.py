import os 
os.system(" cls|| clear")

def calcular_media(nota1, nota2):
    soma = nota1 + nota2 
    resultado = soma / 2 
    return resultado

def verificar_resultado(media):
    if media >= 7:
        print("Aprovado. ") 
    else:
        print("Reprovado.")

print(f"\t= NOTAS = ")
nota1 = float (int(input(f"\nDigite sua 1ª nota:")))
nota2 = float (int(input(f"\nDigite sua 2ª nota:")))

media = calcular_media(nota1, nota2)
verificar_resultado(media)