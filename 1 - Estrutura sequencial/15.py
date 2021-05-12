"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

 
-----------------------
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
------------------------
"""

ganhoH = float(input("quanto você ganha por hora?: "))
horasT = int(input("quantas horas trabalhadas este mês?: "))

salarioM = ganhoH * horasT

IR = (11*salarioM) / 100
INSS = (8*salarioM) / 100
sindicato = (5*salarioM) / 100
liquido = salarioM- (IR+INSS+sindicato)


print("      tabela")
print("-----------------------")
print("+ salario bruto: R$", salarioM)
print("- IR(11%): R$", IR)
print("- INSS(8%): R$", INSS)
print("- sindicato:(5%): R$", sindicato)
print("= liquido: R$", liquido)
print("-----------------------")
