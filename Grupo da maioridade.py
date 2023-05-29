# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
menoridade = 0
maioridade = 0
for i in range(1,8):
  ano = int(input(f"Qual o ano de nascimento da pessoa {i}? "))
  if atual-ano >= 18:
    maioridade += 1
  else:
    menoridade += 1

print(f"\nQuantidade de pessoas que já atingiram a maioridade: {maioridade}")
print(f"Quantidade de pessoas que ainda não são de maior: {menoridade}")
