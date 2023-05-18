# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

total = 0
number = int(input("Digite um número inteiro: "))
for i in range(1, number + 1):
  if number % i == 0:
    total += 1
if total == 2:
  print("Esse número é primo!")
else:
  print("Esse número não é primo.")
  
