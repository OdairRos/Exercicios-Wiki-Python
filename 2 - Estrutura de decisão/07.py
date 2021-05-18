#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input("valor1: "))
num2 = float(input("valor2: "))
num3 = float(input("valor3: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior")
if num1 < num2 and num1 < num3:
    print(f"{num1} é o menor")

if num2 > num1 and num2 > num3:
    print(f"{num2} é o maior")
if num2 < num1 and num2 < num3:
    print(f"{num2} é o menor")

if num3 > num1 and num3 > num2:
    print(f"{num3} é o maior")
if num3 < num1 and num3 < num2:
    print(f"{num3} é o menor")
