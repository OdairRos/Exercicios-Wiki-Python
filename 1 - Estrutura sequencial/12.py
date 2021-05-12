#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = int(input("digite sua altura em cm²: "))
altura = altura /100

pesoIdeal = (72.7*altura) - 58

print("seu peso ideal é:", pesoIdeal)
