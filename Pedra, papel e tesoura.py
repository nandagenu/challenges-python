# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
print("JOKENPÔ!")
op_user = int(input("Escolha uma das opções abaixo:\n1) PEDRA\n2) PAPEL\n3) TESOURA\nResposta: "))
op_pc = choice([1, 2, 3])

if op_pc == 1 and op_user ==1:
    print("O computador escolheu PEDRA e você escolheu PEDRA. Empate!")
elif op_pc == 1 and op_user ==2:
    print("O computador escolheu PEDRA e você escolheu PAPEL. Você ganhou, parabéns!")
elif op_pc == 1 and op_user ==3:
    print("O computador escolheu PEDRA e você escolheu TESOURA. Você perdeu!")

elif op_pc == 2 and op_user ==1:
    print("O computador escolheu PAPEL e você escolheu PEDRA. Você perdeu!")
elif op_pc == 2 and op_user ==2:
    print("O computador escolheu PAPEL e você escolheu PAPEL. Empate!")
elif op_pc == 2 and op_user ==3:
    print("O computador escolheu PAPEL e você escolheu TESOURA. Você ganhou, parabéns!")

elif op_pc == 3 and op_user ==1:
    print("O computador escolheu TESOURA e você escolheu PEDRA. Você ganhou, parabéns!")
elif op_pc == 3 and op_user ==2:
    print("O computador escolheu TESOURA e você escolheu PAPEL. Você perdeu!")
elif op_pc == 3 and op_user ==3:
    print("O computador escolheu TESOURA e você escolheu TESOURA. Empate!")
else:
    print("Opção inválida, tente novamente.")
