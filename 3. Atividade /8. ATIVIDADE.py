import os 
os.system ("clear") 
 
Idade = int (input("Digite sua idade: " ))

if Idade < 18 or Idade > 65:
    print ("Não pode votar")
else: 
    print ("É obrigado a votar!")
if Idade >= 18 and Idade <= 65:
    resultado = "É obrigado a votar!"
else: 
    resultado = "Não pode votar"

# Saída
print(f"\nResultado: {resultado}")