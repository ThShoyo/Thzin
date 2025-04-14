import os 
os.system ("cls || clear")

def inflacionar(preco): 
    if preco < 100: 
        resultado = preco *1.10 #inflacionar 10%
    else:
        resultado = preco * 1.20 #inflacionar 20%
    return resultado

preco_produto = float(input("Digite o preco do produto: "))

preco_inflacionado = inflacionar(preco_produto)

print(f"Preço com aumento: {preco_inflacionado}")

