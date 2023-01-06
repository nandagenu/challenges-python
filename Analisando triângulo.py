# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print("Digite 3 valores para formar um triângulo.")
r1 = int(input("Primeiro valor: "))
r2 = int(input("Primeiro valor: "))
r3 = int(input("Primeiro valor: "))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print("Os valores digitados podem formar um triângulo.")
else:
    print("Não é possível formar um triângulo com esses valores. Tente novamente.")
