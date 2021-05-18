"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

"""
#ax2 + bx + c
# x = a*2 + b + c

a = float(input('a: '))
if a == 0:
    print('não é uma equação de segundo grau')
else: 
    b = float(input('b: '))
    c = float(input('c: '))
    delta = b**2 - 4*a*c
    if delta < 0:
        print('a equação não possui raizes reais')
    elif delta == 0:
        print("Há apenas uma raíz real igual a", -b/(2*a))
    else:
        print('a equação possui duas raiz reais')
        print("Raíz 1:", (-b+delta**(1/2))/(2*a))
        print("Raíz 2:", (-b-delta**(1/2))/(2*a))
