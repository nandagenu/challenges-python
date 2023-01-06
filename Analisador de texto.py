# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: ")).strip()
print(f"Nome com todas as letras maísculas: {nome.upper}")
print(f"Nome com todas as letras minúsculas: {nome.lower}")
print(f"Total de letras do nome: {len(nome) - nome.count(' ')}")
separa = nome.split()
print(f"Total de letras do primeiro nome: {separa[0], len(separa[0])}")
