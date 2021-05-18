#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

valor = int(input('Valor: '))

if valor == 0:
    print(f'{valor} é nulo')
elif valor % 2 == 0:
    print(f'{valor} é par')
else:
    print(f'{valor} é impar')