# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input("Qual a velocidade do carro? "))
multa = (vel - 80)*7

if vel > 80:
    print("Você foi multado.")
    print(f"A sua multa será de R${multa}!")
else:
    print("Você está dentro da velocidade limite.")
