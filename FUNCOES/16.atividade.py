import os 
os.system("cls || clear")

def calcular_imc(peso, altura):
    return peso / (altura * altura)

def situacao(imc):
    if imc >= 40: 
        classificacao = "Obeseidade garau III"
        recomendacao = "Busque assistência médica imediatamente."
    elif imc >= 35: 
        classificacao = "Obesidade grau II"
        recomendacao = "Consute um médico para avaliação e orientação."
    elif imc >= 30:
        classificacao = "Obesidade grau I"
        recomendacao = "Procure orientação de um profisional de saúde."
    elif imc >= 25:
        classificacao = "Sobrepeso"
        recomendacao = "Considere uma dieta balanceada e atividade física."
    elif imc >= 18.5:
        classificacao = "Peso normal"
        recomendacao = "Mantenha hábitos saudaveis."
    else:
        classificacao = "Abaixo do peso"
        recomendacao = "Considere uma avaliação médica."
    return classificacao, recomendacao