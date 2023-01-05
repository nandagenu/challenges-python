# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input("Quanto dinheiro você tem na carteira, em reais? R$"))
dolar = dinheiro/5.28

# A cotação de 5,28 equivale ao valor do dia 27/12/2022.

print(f"O valor de R${dinheiro} que você tem na carteira, equivale em dólares a ${dolar:.2f}.")
