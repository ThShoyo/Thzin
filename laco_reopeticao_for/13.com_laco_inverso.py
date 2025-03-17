import os 
os.system("cls || clear")

soma = 0

print("NOTAS:")
for i in range(3):
    nota = float(input(f"Digite uma nota: "))
    soma += nota 


media = soma / 3

print(f"media: {media}")
   
if media >= 7:
    print ("Aprovado")
if media <= 4:
    print ("Reprovado")