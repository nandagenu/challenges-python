# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 'a'
while sexo not in 'MF':
  sexo = str(input("Digite o sexo da pessoa, apenas entre 'M' ou 'F': ")).upper()
  if sexo not in 'MF':
    print("Resposta inválida. Tente novamente.\n")
  else:
    print(f"Sexo {sexo} registrado com sucesso!")

# OR

'''
sexo = None
while sexo != 'M' and sexo != 'F':
  sexo = str(input("Digite o sexo da pessoa, apenas entre 'M' ou 'F': ")).upper()
  if sexo != 'M' and sexo != 'F':
    print("Resposta inválida. Tente novamente.\n")
  else:
    print(f"Sexo {sexo} registrado com sucesso!")'''
