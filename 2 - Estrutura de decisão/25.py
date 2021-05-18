"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

pergunta1 = input('Telefonou para a vitima?[S-sim/N-não]: ').upper()
pergunta2 = input('Esteve no local do crime?[S-sim/N-não]: ').upper()
pergunta3 = input('Mora perto da vitima?[S-sim/N-não]: ').upper()
pergunta4 = input('Devia para vitima?[S-sim/N-não]: ').upper()
pergunta5 = input('Ja trabalhou com a vitima?[S-sim/N-não]: ').upper()

Sim = int(0)

if pergunta1[0] == 'S':Sim += 1
if pergunta2[0] == 'S':Sim += 1
if pergunta3[0] == 'S':Sim += 1
if pergunta4[0] == 'S':Sim += 1
if pergunta5[0] == 'S':Sim += 1

if Sim == 2:
    print('Classificação: Suspeita')
elif Sim == 3 or Sim == 4:
    print('Classificação: Cúmplice')
elif Sim == 5:
    print('Classificação: Assasino')
else:
    print('Classificação: Inocente')