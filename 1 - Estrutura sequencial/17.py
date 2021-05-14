"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

import math
tamanho = float(input("quantos m² tem a area a ser pintada: "))#109

Litro = float(6)
Lata = 80 #preço

galao = 25 #preço

lata_qt = math.ceil(tamanho / (Litro*18))
lata_pr = lata_qt * Lata
print("comprando apenas latas de 18 litros: R$",lata_pr)
print("quantidade de latas a serem compradas: ",lata_qt)

galao_qt = math.ceil(tamanho / (Litro*3.6))
galao_pr = galao_qt * galao
print("\ncomprando apenas galoes de 3.6 litros: R$", galao_pr)
print("quantidade de galoles  ser  comprados: ", galao_qt)


lata_qt = math.floor(tamanho / (Litro * 18))
lata_pr = lata_qt*80

tamanho -= lata_qt*(Litro*18)

galao_qt = math.ceil(tamanho / (Litro*3.6))
galao_pr = galao_qt * 25
print(f"\nmesclando entre galoes e latas: R$", galao_pr+lata_pr)
print(f"latas: {lata_qt} e galoes: {galao_qt}")

