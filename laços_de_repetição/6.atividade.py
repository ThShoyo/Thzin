import os 
import time

os.system("cls | clear")

contador  = 0 
soma_salario = 0 
maior_idade = 0 
menor_idade = 9999 
mulheres5k = 0 

while True:
    print("""
CÓDIGO | DESCRIÇÃO
  1    | ADICIONAR PESSOA 
  2    | EXIBIR RESULTADOS 
  3    | SAIR    
 """)   

    opcao = int(input("ESCOLHA 1 | 2 | 3  PARA A OPÇÃO DESEJADA: ")) 

    match opcao:
        case 1 :  
            idade = int(input("Digite sua idade: "))
            sexo = (input("Digite 'M' ou 'F' para o seu sexo: ")) .upper()        
            salario = float(input("Digite o seu salário: "))
            contador += 1
            soma_salario += salario 
            maior_idade = max (maior_idade)
            menor_idade = min (menor_idade)
            if sexo == "F" and salario >= 5000:
                mulheres5k += 1
            os.system("cls || clear")
        case 2:
            if contador > 0: 
                media_salarial = soma_salario / contador 
                print("\n= Exibindo resultados = ")
                print(f"Média salarial do grupo : {media_salarial}  ")
                print(f"Maior idade do grupo: {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Quantidade de mulheres com salário a partir de 5k: {mulheres5k}")
            else: 
                print("\nNão foram informados os dados necessários.")
            time.sleep(3)
            os.system("cls || clear")
        case 3: 
            print("\n= FIM =")
            break
        case _:
            (f"\nOpçao inválida!")
            time.sleep(3)
            os.system("cls|| clear") 
