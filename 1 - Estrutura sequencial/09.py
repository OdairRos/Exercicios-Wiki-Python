#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

tempF = int(input("temperatura em graus Fahrenheit: "))

tempC = 5 * ((tempF-32) / 9)

print("{0} graus Fahrenheit em graus Celsius: {1}".format(tempF, tempC))
