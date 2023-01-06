# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#number = float(input("Digite um número real qualquer: "))
#print(f"A porção inteira do valor {number} será {number:.0f}")

#OU

from math import trunc
number = float(input("Digite um valor real qualquer (com vírgula): "))
print(f"O valor digitado foi {number} e a sua porção inteira é {trunc(number)}")
