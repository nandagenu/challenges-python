# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print("Digite abaixo três números distintos.")
n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Terceiro número: "))

if n3==n2 or n3==n1 or n1==n2:
    print("Você digitou números repetidos, tente novamente.")

elif n1 > (n2 and n3) and n2 < (n1 and n3):
    print(f"O número {n1} é o maior e o número {n2} é o menor entre todos.")
elif n1 > (n2 and n3) and n3 < (n1 and n2):
    print(f"O número {n1} é o maior e o número {n3} é o menor entre todos.")
    
elif n2 > (n1 and n3) and n1 < (n2 and n3):
    print(f"O número {n2} é o maior e o número {n1} é o menor entre todos.")
elif n2 > (n1 and n3) and n3 < (n2 and n1):
    print(f"O número {n2} é o maior e o número {n3} é o menor entre todos.")

elif n3 > (n1 and n2) and n1 < (n2 and n3):
    print(f"O número {n3} é o maior e o número {n1} é o menor entre todos.")
elif n3 > (n1 and n2) and n2 < (n1 and n3):
    print(f"O número {n3} é o maior e o número {n2} é o menor entre todos.")
