"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

salario = float(input("Digite seu salario: "))
print(f"salario antes: R${salario}")

if salario < 280 and salario >= 0:
    aumento = ((salario * 20) / 100)
    salario = ((salario *120)/ 100)
    print("Aumendo de: 20%")
    print("Valor de aumento: ", )
    
elif salario >= 280 and salario < 700:
    aumento = ((salario * 15) / 100)
    salario = ((salario * 115) / 100)
    print("Aumento de: 15%")
    
elif salario >= 700 and salario < 1500:
    aumento = ((salario * 10) / 100)
    salario = ((salario * 110) / 100)
    print("Aumento de: 10%")
    
elif salario > 1500:
    aumento = ((salario * 5)/ 100)
    salario =((salario * 105) / 100)
    print("Aumento de: 5%")

else:
    print('há algo errado')


print(f"Valor de aumento: R${aumento}")
print(f"salario depois: R${salario}")
