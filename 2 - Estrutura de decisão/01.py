#Faça um Programa que peça dois números e imprima o maior deles.

num1 = float(input("Digite um valor: "))
num2 = float(input("digite um valor: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}")
else:
    print(f"{num2} é maior que {num1}")
