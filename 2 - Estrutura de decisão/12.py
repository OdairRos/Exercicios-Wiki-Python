"""
faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.

No exemplo o valor da hora é 5 e a quantidade de hora é 220.

 Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
        
"""

hora = float(input("Quanto você ganha por Hora: "))
m_horas = int(input("Quantas horas trabalhou no mês: "))

salario = hora * m_horas
print(f"\n Bruto : R${salario}")

if salario <= 900 and salario > 0:
    print('IR(isento) : R$0,00')
elif  salario <= 1500:
    IR = ((5 * salario) / 100)
    print('IR(5%) : R$', IR)
elif salario  <= 2500:
    IR = ((10 * salario)/100)
    print('IR(10%) : R$', IR)
elif salario > 2500:
    IR = ((20 * salario)/100)
    print('IR(20%) : R$', IR)
else:
    print('algo de errado aconteceu')
    
salarioLQ = salario - (((10 * salario)/100) + IR)
print('INSS(10%) : R$', ((10 * salario)/100))
print('descontos : R$', ((10 * salario)/100) + IR)
print('liquido : R$', salarioLQ)
