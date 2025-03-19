import os 
os.system("cls \\ clear")

login_cadastrado = "Izabela"
senha_cadastrada = "123"

for i in range(3):
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")

        if login_cadastrado == login and senha_cadastrada == senha:
            print("Bem-vindo")
            break    
        else:
        
            print("Acesso negadoef. \n")
            if i == 2:
                print("Número de tentativas acima do permitido.")

