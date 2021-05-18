#Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia = int(input("valor: "))

if dia == 1:
    print('domingo')
elif dia == 2:
    print('segunda')
elif dia == 3:
    print('terça')
elif dia == 4:
    print('quarta')
elif dia == 5:
    print('quinta')
elif dia == 6:
    print('sexta')
elif dia == 7:
    print('sabado')
else:
    print('valor invalido')
