#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganhoHora = float(input("Quanto você ganha por hora? :"))
Trabalhadas = int(input("Quantas horas trabalhadas no mês? "))

ganhoMes = ganhoHora * Trabalhadas

print(f"Você trabalhou {Trabalhadas}h neste mês, e ganhou R$ {ganhoMes}")
