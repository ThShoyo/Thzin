import os 
os.system("cls || clear")

def converter_centimetros(metros):
    return metros * 100;

print("= CONVERTER CENTÍMETROS PARA CENTÍMETROS = ")
metros = float(input("Digite um número: "))

centimetros = converter_centimetros(metros)

print("\n= RESULTADOS =")
print(f"{metros} metros é igual a {centimetros} centímetros.")