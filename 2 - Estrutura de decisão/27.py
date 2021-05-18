"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
faça um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

morango = float(input('Morango Kg:'))
maca = float(input('Maca Kg:'))

if morango <= 5:
    if (morango + maca) > 8:
        valor =  (morango * 2.5) - (((morango * 2.5) / 100) * 10)
        print(f'morango: {morango}Kg Preço: R${valor}')
    else:
        valor = (morango * 2.5)
        print(f'morango: {morango}Kg Preço: R${valor}')
if morango > 5:
    if (morango + maca) > 8:
        valor = (morango * 2.20) - (((morango * 2.20) / 100) * 10)
        print(f'morango: {morango}Kg Preço: R${valor}')
    else:
        valor = morango * 2.20
        print(f'morango: {morango}Kg Preço: R${valor}')
        
if maca <= 5:
    if (morango + maca) > 8:
        valor = (maca * 1.8) - (((maca * 1.8) / 100)* 10) 
        print(f'Maçã: {maca}Kg Preço: R${valor}')
    else:
        valor = maca * 1.8
        print(f'Maçã: {maca}Kg Preço: R${valor}')
if maca > 5:
    if (morango + maca) > 8:
        valor = (maca * 1.5) - (((maca * 1.5) / 100) * 10)
        print(f'Maçã: {maca}Kg Preço: R${valor}')
    else:
        valor = maca * 1.5
        print(f'Maçã: {maca}Kg Preço: R${valor}')
