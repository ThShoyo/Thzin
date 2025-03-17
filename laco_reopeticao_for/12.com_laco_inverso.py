import os 

os.system("cls || clear")

soma = 0

print("NOTAS:")
for i in range(4):
    nota = float(input(f"Digite uma nota: "))
    soma += nota 

media = soma / 4

print()
print(f"Média: {media}")


print("\nFM DO PROGRAMA")