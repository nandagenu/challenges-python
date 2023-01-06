# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Digite a quantidade de Km percorridos pelo carro alugado: "))
dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))
preço = 0.15*km + dias*60
print(f"O preço a ser pago, de acordo com a quantidade de dias e km rodados, será de R${preço:.2f}.")
