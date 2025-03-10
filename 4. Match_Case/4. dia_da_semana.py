import os
os.system ("clear")

dia = int (input("Digite um número: "))

match dia: 
    case 1: 
        print ("Domingo \t fim de semana")
    case 2: 
        print ("Segunda \t Dia útil")
    case 3: 
        print ("Terça \t Dia útil") 
    case 4: 
        print ("Quarta \t Dia útil") 
    case 5: 
        print ("Quinta \t Dia útil") 
    case 6: 
        print ("Sexta \t Dia útil") 
    case 7: 
        print ("Sábado \t fim de semana") 

