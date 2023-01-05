# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input("Digite o valor de um comprimento, em metros: "))
cent = metro * 100
mili = metro * 1000

print(f"O valor do comprimento, convertido em centímetros e milímetros, respectivamente, é de {cent} e {mili}.")
