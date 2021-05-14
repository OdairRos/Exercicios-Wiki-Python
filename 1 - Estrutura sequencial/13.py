#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#1- Para homens: (72.7*h) - 58
#2- Para mulheres: (62.1*h) - 44.7

altura = float(input("digite sua altura em cm²: "))
altura = altura/100

homen = (72.7*altura) - 58
mulher = (62.1*altura) - 44.7

print("\nse você for homen seu peso ideal é:", homen)
print("mas caso você seja mulher seu peso ideal é:", mulher)
