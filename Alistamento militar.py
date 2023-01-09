# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano_nasc = int(input("Qual o seu ano de nascimento? "))
ano_atual = 2023

# O código foi criado no ano de 2023.

if (ano_atual - ano_nasc) < 18:
    print("Você ainda vai se alistar ao serviço militar.")
    print(f"Faltam {18 - (ano_atual - ano_nasc)} anos para o alistamento. ")
elif (ano_atual - ano_nasc) == 18:
    print("Está na hora exata de se alistar.")
elif (ano_atual - ano_nasc) > 18:
    print("Já passou do tempo do alistamento.")
    print(f"Já se passaram {(ano_atual - ano_nasc) - 18} anos do prazo de alistamento.")
