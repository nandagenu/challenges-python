# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input("Digite o seu nome: ")).strip().upper()
print(f"Existe a palavra SILVA no nome?\nTrue para SIM ou False para NÃO\nR = {'SILVA' in nome}")
