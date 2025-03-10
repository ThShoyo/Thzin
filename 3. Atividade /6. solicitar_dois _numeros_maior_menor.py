import os 
os.system ("clear")

num_um = int (input("Digite o primeiro número: "))
num_dois = int (input("Digite o seu segundo número: "))

maior = max(num_um, num_dois)
menor = min(num_um, num_dois)

if num_um == num_dois:
    print ("Os números são iguais")
else :
    print ("Não são iguais")

print (f"O primeiro número é: {num_um}")
print (f"O segundo número é: {num_dois}")
print (f"O maior número é: {maior}")
print (f"O menor número é: {menor}")