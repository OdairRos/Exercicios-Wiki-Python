"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

num1 = float(input('Valor1: '))
num2 = float(input('Valor2: '))
x = float(0)

operação = input('M-multiplicação\nD-divisão\nSO-soma\nSU-subtração:').upper()

if operação == 'M':
    x = num1 * num2
elif operação == 'D':
    x = num1 / num2
elif operação == 'SO':
    x = num1 + num2
elif operação == 'SU':
    x = num1 - num2

if x != 0:
    if x % 2 == 0:
        final = f'{x} é: par, '
    else: 
        final = f'{x} é: impar, '
    
    if x > 0:
        final += 'positivo, '
    else: 
        final += 'negativo, '

    if x % 1 == 0:
        final += 'inteiro'
    else:
        final += 'decimal'
    print(final)
else:
    print('Por favor, digite a entrada correta.')
