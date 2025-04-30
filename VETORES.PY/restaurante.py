import os 
os.system("cls || clear")

lista_pratos = []
precos_pratos = []

soma = 0 
while True:
    print("""
        Código \t Prato \t\t\t Valor
        1 \t Picanha \t\t R$ 25,00 
        2 \t Lasanha \t\t R$ 20,00
        3 \t Strognoff \t\t R$ 18,00   
        4 \t Bife acebolado \t  R$ 15,00 
        5 \t Pão com ovo \t\t R$ 5,00

""")
    opcao = int(input("Digite o numero da opção desejada:"))

    match opcao:                                     
        case 1:
            prato = "Picanha"
            preco = 25,00
        case 2: 
            prato = "Lasanha"
            preco = 20,00
        case 3:
            prato = "Strognoff" 
            preco = 18,00
        case 4: 
            prato = "Bife acebolado" 
            preco = 15,00   
        case 5:
            prato = "Pão com ovo" 
            preco = 5,00
        case _:
            print ("Opção invalida. \nTente novamente. \n")
    if opcao >= 1 and opcao <= 5:
        lista_pratos.append(prato)
        precos_pratos.append(preco)

    continuar = input("Deseja escolher outro prato? \n Responda com 'S' ou 'N' ").lower()
    if continuar == "n":
        break
    os.system("cls || clear")

if sum(precos_pratos) == 0:
    print("\nNenhum prato foi selecionado")
else:
    print("\n=PRATOS ESCOLHIDOS =")
    for i, prato in enumerate(lista_pratos, start=1):
        print(f"{i}º prato: {prato}")

    print(f"\nTotal: R$ {sum(precos_pratos):.2f}")

print("\n= Volte sempre! =")