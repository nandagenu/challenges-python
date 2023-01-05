# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input("Digite o primeiro número. "))
n2 = float(input("Digite o segundo número. "))
n3 = float(input("Digite o terceiro número. "))

if n1 > (n2 and n3):
    print(f"O número {n1} é o maior entre todos.")
elif n2 > (n1 and n3):
    print(f"O número {n2} é o maior entre todos.")
elif n3 > (n1 and n2):
    print(f"O número {n3} é o maior entre todos.")

if n1 < (n2 and n3):
    print(f"O número {n1} é o menor entre todos.")
elif n2 < (n1 and n3):
    print(f"O número {n2} é o menor entre todos.")
elif n3 < (n1 and n2):
    print(f"O número {n3} é o menor entre todos.")
elif n3 == n2 == n1:
    print("Você digitou números repetidos, tente novamente.")
