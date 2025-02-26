import os
os.system ("clear")







# Entrada
opcao = int(input("""
Código \t Prato \t\t\t Valor
1 \t Picanha \t\t R$ 25,00 
2 \t Lasanha \t\t R$ 20,00
3 \t Strognoff \t\t R$ 18,00   
4 \t Bife acebolado \t  R$ 15,00 
5 \t Pão com ovo \t\t R$ 5,00

Digite a opção desejada:
"""))

# Processamento 
match opcao:                                     
    case 1:
        print ("Opção desejada: Picanha, 25,00")
    case 2: 
        print ("Opção desejada: Lasanha, 20,00")    
    case 3:
        print ("Opção desejada: Strognoff, 18,00")
    case 4: 
        print ("Opção desejada: Bife acebolado, 15,00")    
    case 5:
        print ("Opção desejada: Pão com ovo, 5,00")
    case _:
        print ("Opção invalida")
        


# Saída