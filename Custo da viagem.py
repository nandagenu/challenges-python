# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

km = int(input("Qual a distância da viagem, em km? "))
preço1 = 0.5*km
preço2 = 0.45*km

if km <= 200:
    print(f"O preço da passagem será de R${preço1} reais.")
else:
    print(f"O preço da passagem será de R${preço2} reais.")
