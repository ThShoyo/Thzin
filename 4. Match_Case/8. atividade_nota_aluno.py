import os 
os.system ("clear")

nome = str(input("Digite o seu nomne: "))
Nota_1 = float(input("Digite sua primeira nota"))
Nota_2 = float(input("Digite sua segunda nota"))

soma = Nota_1 + Nota_2
media = soma / 2

print (f"media: {media}")

if media > 6: 
    print  ("Aprovado")
if media < 4: 
    print ("Reprovado")