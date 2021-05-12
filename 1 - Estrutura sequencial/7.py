#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário

lado = float(input("qual medida do lado em cm?: "))
base = float(input("qual medida da base em cm?: "))

area = base*lado

print("a area do quadrado é: ", area, "cm² e o dobro é:", area*2,"cm²")
