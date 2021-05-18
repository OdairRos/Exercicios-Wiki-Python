#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("digite uma letra: ")).upper()

if letra[0] == 'A' or letra[0] == 'E' or letra[0] == 'I' or letra[0] == 'O' or letra[0] == 'U':
    print("A letra digitada é uma vogal")
else:
    print("A letra digitada é uma consoante")
