# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

c = 0
for i in range(0, 501):
    c = c + i
print(f"A soma de todos os valores entre 1 e 500 é igual a {c}")
