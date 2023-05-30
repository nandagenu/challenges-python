# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
qtd = 0
mais_velho = 0
for i in range (1,5):
  nome = str(input(f"Qual o nome da pessoa {i}? "))
  idade = int(input(f"Qual a idade da pessoa {i}? "))
  soma_idade += idade
  sexo = int(input(f"Qual o sexo da pessoa {i}? Digite 1 para MULHER ou 2 para HOMEM: "))
  print("\n")
  if idade < 20 and sexo == 1:
    qtd += 1
  if i == 1 and sexo == 2:
    mais_velho = idade
  elif sexo == 2 and idade > mais_velho:
    mais_velho = idade
    nome_homem = nome
print(f"A média da idade do grupo é de {soma_idade/4} anos.")
print(f"O nome do homem mais velho do grupo é {nome_homem}.")
print(f"Quantidade de mulheres com idade menor que 20: {qtd}")
