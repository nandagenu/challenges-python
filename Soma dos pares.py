# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

'''import random
c = 0

print("Gerando números aleatórios de 1 a 100.\n")
for i in range(6):
  number = random.randint(0, 101)
  print(f"Número {i+1}: {number}")
  if number % 2 == 0:
      c += number
      print(f"Esse número é par.\nSoma dos números até agora: {c}\n")
  else:
      print("O número é ímpar e será desconsiderado na soma.\n")
      
OU '''

c = 0
print("Informe abaixo 6 números inteiros aleatórios.\n")
for i in range(6):
  number = int(input(f"Digite o {i+1}º número: "))
  if number % 2 == 0:
      c += number
      print(f"Esse número é par.\nSoma dos números até agora: {c}\n")
  else:
      print("O número é ímpar e será desconsiderado na soma.\n")
