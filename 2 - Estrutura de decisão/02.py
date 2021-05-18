#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num1 = float(input("digite um valor: "))

if num1 < 0:
    print(f"{num1} é negativo")
elif num1 == 0:
    print("0(zero)é neutro/nulo")
else:
    print(f"{num1} é positivo")
