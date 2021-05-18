#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

import math

numero = float(input('valor: '))

if numero % 1 == 0:
    print(f'{numero} é um inteiro.')
else:
    print(f'{numero} é um decimal.')