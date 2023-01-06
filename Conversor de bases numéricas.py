# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro qualquer: "))
base = int(input("Escolha qual será a base de conversão.\n1 para BINÁRIO\n2 para OCTAL\n3 para HEXADECIMAL\nResposta: "))

if base == 1:
    print(f"{num} para binário: {bin(num)[2:]}")
elif base == 2:
    print(f"{num} para binário: {oct(num)[2:]}")
elif base == 3:
    print(f"{num} para binário: {hex(num)[2:]}")
else:
    print("Número inválido. Tente novamente.")
