import os 

os.system ("cls || clear")

soma = 0 
contador = 0



while True:

    print("""
CÓDIGO | DESCRIÇÃO
  1    |
  2    |
  3    |    
 """)   

    opcao = int(input()) 

    match opcao:
        case 1 : 
            int(input("Digite sua idade: "))
            (input("Digite 'M' ou 'F' para o seu sexo: "))        
            float(input("Digite o seu salário: "))

        case 2:
            # Mostre os resultados.
        case 3: 
            # Pare.
        case _:
            (f"\nOpçao inválida")








