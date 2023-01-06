# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

number = str(input("Digite um número inteiro, entre 0 e 9999: ")).zfill(4)

print(f"Primeiro dígito: {number[0]}")
print(f"Segundo dígito: {number[1]}")
print(f"Terceiro dígito: {number[2]}")
print(f"Quarto dígito: {number[3]}")
