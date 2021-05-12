"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidadede um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""


tamanho = float(input("qual tamanho do aquivo em MB: "))
velocidade = float(input("qual valocidade em Mbps: "))

tempo = tamanho / velocidade
print(f"ira demorar {tempo/60} segundos")
