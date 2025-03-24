
import os 
os.system("clear")






# Entrada
primeiro_numero =
operador = input("Digite a operaçao que deseja(+ - * /): ")
segundo_numero = int(input("Digite um número: "))

#Processamneto
match operador:
    case "+": 
        resultado = primeiro_numero + segundo_mumero
    case "-": 
        resultado = primeiro_numero - segundo_mumero
    case "*": 
        resultado = primeiro_numero * segundo_mumero
    case "/":
        resultado = primeiro_numero / segundo_mumero    

    case _:
        resultado = "opção invalida"

# Saída
print (f"Primeiro número: {primeiro_numero}")
print (f"Operação: {operador}")
print (f"Segundo número: {segundo_numero} ")
print (f"Resultado: {resultado}")