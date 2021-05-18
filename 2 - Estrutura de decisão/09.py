#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("valor1: "))
num2 = float(input("valor2: "))
num3 = float(input("valor3: "))

if num1 > num2 and num1 > num3:
    print(num1)
    if num2 > num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
if num2 > num1 and num2 > num3:
    print(num2)
    if num1 > num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
if num3 > num1 and num3 > num2:
    print(num3)
    if num1 > num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)
    
