#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#1 - o produto do dobro do primeiro com metade do segundo .
#2 - a soma do triplo do primeiro com o terceiro.
#3 - o terceiro elevado ao cubo.

num1 = int(input("diite o numero1(inteiro): "))
num2 = int(input("digite o numero2(inteiro): "))
num3 = float(input("digite o numero3(real): "))

um = (num1*2) + (num2/2)
dois = (num1*3) + num3
tres = num3**3

print("o produto do dobro do primeiro com metade do segundo: {}".format(um))
print('a soma do triplo do primeiro com o terceiro: {}'.format(dois))
print("o terceiro elevado ao cubo: {}".format(tres))
