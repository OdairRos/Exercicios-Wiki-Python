#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input('numero: '))

if ano % 4 == 0:
    print(f' o ano de {ano} é bissexto')
else:
    print('este ano não é bissexto')
