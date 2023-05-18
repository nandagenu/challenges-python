# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print("Vamos calcular os 10 primeiros termos de uma PA.")
pt = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))

for i in range(1, 11):
  print(f"Termo {i}: {pt+i*r}")

#OU
#decimo = pt + 9*r
#for i in range(pt, decimo + r, r):
#  print(i)
