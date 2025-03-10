import os
os.system ("clear")

primeira_nota = float (input("Digite a nota: "))
segunda_nota = float (input("Digite a nota: "))
media = (primeira_nota + segunda_nota) /2

if media >= 9: 
    conceito = "A"
elif media >= 7.5: 
    conceito = "B" 
elif media >= 6: 
    conceito = "C"
elif media >= 4:
    conceito = "D"
else: 
    conceito = "E" 
    
match conceito: 
    case "A" | "B" | "C":
        print (f"Media: {media}")
        print (f"Conceito: (conceito)")
        print ("Aprovado.")
    
    case "D" | "E": 
        print (f"Media: {media}")
        print(f"Conceito: (conceito)")     
        print("Reprovado.")
    case _: 
        print ("Opção inválida.")    