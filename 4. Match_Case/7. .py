# Limpar o terminal.
import os
os.system ("clear")

# Entrada
altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo: ")

# Processamneto
match sexo:
    case  "M" | "m":
        peso_ideal = (72.7 *altura) - 58
        print(f"\nPeso ideal: {peso_ideal}")
    case  "F" | "m":
        peso_ideal = (62.1 * altura) - 44.7
        print(f"nPeso ideal: {peso_ideal}")