import os 
os.system("cls \\ clear")

login_cadastrado = "Izabela"
senha_cadastrada = "123"
contador = 0

while True:
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")
    
        if login_cadastrado == login and senha_cadastrada == senha:
            print("Bem-vindo")
            break    
        else:
            print("Acesso negado. \n")
            contador += 1

            if contador == 3:
                print("Número de tentativas acima do permitido.")
                break