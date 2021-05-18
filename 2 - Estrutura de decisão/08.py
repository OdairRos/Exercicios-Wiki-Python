#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

prod1 = float(input("preço: "))
prod2 = float(input("preço: "))
prod3 = float(input("preço: "))

if prod1 < prod2:
    if prod1 < prod3:
        print(f"produto 1 mais barato: R${prod1}")
    else:
        print(f"produto 3 mais barato: R${prod3}")
else:
    if prod2 < prod3:
        print(f"produto 2 mais barato: R${prod2}")
    else:
        print(f"produto 3 mais barato: R${prod3}")
