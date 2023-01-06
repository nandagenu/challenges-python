# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

'''co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hip = (co**2 + ca**2)**1/2
print(f"O valor da hipotenusa de um triângulo retângulo com cateto oposto = {co} e cateto adjacente = {ca} equivale a {hip}.")

OU'''

from math import hypot
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hip = hypot(co, ca)
print(f"O valor da hipotenusa de um triângulo retângulo com cateto oposto = {co} e cateto adjacente = {ca} equivale a {hip:.2f}.")
