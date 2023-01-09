# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

# O código foi criado no ano de 2023.

ano_nasc = int(input("Qual o ano de nascimento do atleta? "))
idade = 2023 - ano_nasc

if idade <= 9:
    print("Categoria: MIRIM")
elif 14>=idade>9:
    print("Categoria: INFANTIL")
elif 19>=idade>14:
    print("Categoria: JÚNIOR")
elif 25>=idade>19:
    print("Categoria: SÊNIOR")
else:
    print("Categoria: MASTER")
