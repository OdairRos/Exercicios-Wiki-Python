"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:

 Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se
o conceito for D ou E.
"""

nota1 = int(input('nota1: '))
nota2 = int(input('nota2: '))


media = (nota1 + nota2)/ 2
print(f'media: {media}')
    
conceito = str()
pr = str()

if media >= 9 and media <= 10:
    conceito = 'A'
    pr = 'APROVADO'
    
if media < 9 and  media >= 7.5 :
    conceito = 'B'
    pr  = 'APROVADO'
    
if media < 7.5 and media >= 6:
    conceito = 'C'
    pr = 'APROVADO'

if media >=  4 and media < 6:
    conceito = 'D'
    pr = 'REPROVADO'
if media < 4:
    conceito = 'E'
    pr = 'REPROVADO'

print(f'Condição: {pr}\nconceito: {conceito}')

