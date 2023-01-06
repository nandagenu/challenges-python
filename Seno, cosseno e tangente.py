# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
ang = float(input("Digite o valor do ângulo desejado: "))
print(f"O seno do ângulo {ang} equivale a {sin(radians(ang)):.2f}.")
print(f"O cosseno do ângulo {ang} equivale a {cos(radians(ang)):.2f}.")
print(f"A tangente do ângulo {ang} equivale a {tan(radians(ang)):.2f}.")
