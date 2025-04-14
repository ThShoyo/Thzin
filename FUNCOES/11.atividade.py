import os
os.system("cls || clear")


def valores():
    print(f"\t)")

def somar (n1, n2 ) :
    return n1 + n2 

def subtrair  (n1, n2 ):
    return n1 - n2 

def multiplicar (n1, n2 ):
    return n1 * n2 

def  dividir (n1, n2 ):
    return n1 / n2 

print("=NOTAS =")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

soma = somar(n1, n2) 
subtracao = subtrair(n1, n2)
multiplicacao = multiplicar(n1, n2)
divisao = dividir(n1, n2)

print("\n= RESUTADOS = ")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")




