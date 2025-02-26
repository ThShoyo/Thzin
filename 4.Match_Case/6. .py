import os
os.system ("clear")


# Entrada 
valor = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input("""
1 - A vista
2 - A prazo                               
Digite a forma de pagamento: """))

match forma_de_pagamento: 
    case 1:
    # Aplicando desconto de 10%
        desconto = valor *0.1 
        print ("Pagamento a vista")       
    case 2: 
        print ("Pagamento a prazo")
        parcelas= int(input("Insira a quantidade de parcelas: "))
    match parcelas:  
        case 1:        
          