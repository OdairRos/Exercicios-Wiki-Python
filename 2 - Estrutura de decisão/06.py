#faça um Programa que leia três números e mostre o maior deles.

num1 = float(input("valor 1: "))
num2 = float(input("valor 2: "))
num3 = float(input("valor 3: "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} é o maior")
    else:
        print(f"{num3} é o maior")
elif num2 > num1:
    if num2 > num3:
        print(f"{num2} é o maior")
    else:
        print(f"{num3} é o maior")
