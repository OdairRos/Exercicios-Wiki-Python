"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

litro = float(input("Litros: "))
tipo = input('G- Gasolina ou A-Álcool: ').upper()
gasolina = float(2.5)
alcool = float(1.90)

if tipo == 'G':
    if litro <= 20 and litro > 0:
        preço = litro * (gasolina - (gasolina/100)*4) 
    if litro > 20:
        preço = litro * (gasolina  - (gasolina/100)*6) 
    print(f'valor: {preço} por {litro} litros')
elif tipo == 'A':
    if litro <= 20 and litro > 0:
        preço = litro * (alcool - (alcool/100)*3)
    if litro > 20:
        preço = litro * (alcool -  (alcool/100)*5)
    print(f'Valor: {preço} por {litro} litros')
else:
    print('Por favor, insira os dados corretamente.')