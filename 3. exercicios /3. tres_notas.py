# Limpar o terminal.
import os
os.system("clear")

# Elabore um algoritimo para solicitar ao usuário três notas. 
# Calcule a media do aluno 
# Caso a media do aluno seja menor que 7, o aluno está reprovado. 
# Mostrar: média e se está aprovado ou reprovado.
  
primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))
terceira_nota = float(input("Digite sua terceira nota: "))

soma = primeira_nota + segunda_nota + terceira_nota
media = soma / 3

print(f"Média: {media}")

if media < 7:
    print("Reprovado!")
else:
    print("Aprovado")
