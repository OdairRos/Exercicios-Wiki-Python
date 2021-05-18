#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = str(input('data em dd-mm-aaaa:'))

if int(data[0:1]) > 0 and int(data[0:1]) <= 31:
    if int(data[3:4]) > 0 and int(data[3:4]) <= 12 and data[2] == '-':
        if int(data[6:9]) > 0 and data[5] == '-' :
            print('Esta data é valida!')
        else:
            print('Erro! Data em formato invalido')
    else:
        print('Erro! Data em formato invalido')
else:
    print('Erro! Data em formato invalido')
