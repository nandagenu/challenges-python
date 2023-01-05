# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

frase = str(input("Digite o seu nome completo: ")).strip().split()

print(f"Qual o primeiro nome? {frase[0]}")
print(f"Qual o último nome? {frase[-1]}")
