import os 
os.system("clear")

idade = 16

# se idade < 12 entao
#       escreval("Acesso negado")
# senao se idade < 18 entao
#       escreval("Somente com permissao dos pais.")
# senao
#       escreval("Acesso permitido")
# fimse

if idade < 12:
        print("Acesso negado.")
elif idade < 18:
        print("Somente com a permissao dos pais")
else:        
        print("Acesso permitido.")

print("== FIM ==")