# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

print("Digite 3 valores para formar um triângulo.")
r1 = int(input("Primeiro valor: "))
r2 = int(input("Primeiro valor: "))
r3 = int(input("Primeiro valor: "))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print("Os valores digitados podem formar um triângulo.")
    if r1 == r2 == r3:
        print("O triângulo formado é EQUILÁTERO, pois possui todos os lados iguais.")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("O triângulo formado é ISÓSCELES, pois possui dois lados iguais.")
    elif r1 != r2 != r3:
        print("O triângulo formado é ESCALENO, pois possui todos os lados diferentes.")
else:
    print("Não é possível formar um triângulo com esses valores. Tente novamente.")
