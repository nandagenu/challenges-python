# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre essa variável.

var = input("Digite uma palavra ou valor qualquer. ")

print("Sobre essa variável, vamos analisar as seguintes informações:\n")
print("Qual o tipo da variável?", type(var))
print("Ela só tem espaços?", var.isspace())
print("Ela é de ordem numérica?", var.isnumeric())
print("É alfabético?", var.isalpha())
print("É alfanumérico?", var.isalnum())
print("Está em maiúsculo?", var.isupper())
print("Está em minúsculo?", var.islower())
