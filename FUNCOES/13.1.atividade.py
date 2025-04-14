import os 
os.system ("cls || clear")

def descontar(preco): 
    if preco < 100: 
        resultado = preco * 0.10 
    else:
        resultado = preco * 0.20 
    return resultado

preco_produto = float(input("Digite o preco do produto: "))

preco_descontado = descontar(preco_produto)
preco_final = preco_produto - preco_descontado

print(f"Valor do desconto: {preco_final}")