# Melhore o jogo DESAFIO 028 onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
num = randint(0,10)
resposta = 0
qtd = 0
while resposta != num:
  resposta = int(input("Advinhe qual o número, entre 0 a 10: "))
  qtd += 1
  if resposta > num:
    print("Resposta incorreta, tente um número menor!\n")
  elif resposta < num:
    print("Resposta incorreta, tente um número maior!\n")
print(f"Acertou, o número era {num}! Foram {qtd} tentativas até a resposta correta!")
