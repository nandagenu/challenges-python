# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice
n = int(input("Diga qual o número escolhido pelo computador: "))
n_random = choice([0, 1, 2, 3, 4, 5])

if n_random == n:
    print(f"Parabéns, o número escolhido foi {n}! Você acertou!")
elif n > 5:
    print("Você chutou alto demais, tente novamente.")
elif n < 0:
    print("Você chutou baixo demais, tente novamente.")
else:
    print(f"O número escolhido pelo computador foi {n_random}, e o seu foi {n}!")
    print("Não foi dessa vez. Tente novamente!")
