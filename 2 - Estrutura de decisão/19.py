"""
faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

numero = int(input('valor < 1000:'))

if numero >= 1000: print("Digite um valor menos que Mil")
else:
    numero = str(numero)
    pos = len(numero)
    
    if pos == 3:
        if numero[0] == '1':
            print('centena: ',numero[0])
        else:
            print('centenas: ',numero[0])

        if numero[1] == '1':
            print('dezena: ', numero[1])
        else:
            print('dezenas', numero[1])

        if numero[2] == '1' :
            print('unidade', numero[2])
        else:
            print('unidades', numero[2])
            
    elif pos == 2:
        if numero[0] == '1':
            print('dezena: ', numero[0])
        else:
            print('dezenas', numero[0])

        if numero[1] == '1' :
            print('unidade', numero[1])
        else:
            print('unidades', numero[1])
    elif pos == 1:
        
        if numero[0] == '1' :
            print('unidade', numero[0])
        else:
            print('unidades', numero[0])
