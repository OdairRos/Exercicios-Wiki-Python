#faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input("digite seu sexo[M/F]: "))

if sexo.upper() == 'M':
    print("masculino")
elif sexo.upper() == 'F':
    print("feminino")
else:
    print("sexo invalido")
