"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada 
valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, 
uma nota de 5 e quatro notas de 1.
"""
import math
saque = float(input('Valor de saque: '))
x = saque
if saque  < 10 or saque > 600: 
    print('O valor minimo e maximo  para saque é 10 e 600 reais')
else: 
    cem = cinquenta = dez = cinco = um = int(0)
    if saque >= 100:
        cem = math.floor(saque / 100)#saque atual / valor da nota = quantidade de notas.
        saque = saque - (cem * 100)

    if saque >= 50:
        cinquenta = math.floor(saque/50)
        saque = saque - (cinquenta * 50)
    if saque >= 10:
        dez = math.floor(saque/10)
        saque = saque - (dez*10)
    if saque >= 5:
        cinco = math.floor(saque/5)
        saque = saque - (cinco*5)
    if saque >= 1:
        um = math.ceil(saque/1)
        saque = saque - (um* 1)

    print(f'Valor de saque: R${x}')
    if cem >= 1:
        print(f'notas de 100: {cem}')
    if cinquenta >= 1:
        print(f'notas de 50: {cinquenta}')
    if dez >= 1: 
        print(f'notas de 10: {dez}')
    if cinco >= 1:
        print(f'notas de 5: {cinco}')
    if um >= 1:
        print(f'notas de 1: {um}')

