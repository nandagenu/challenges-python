# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual o valor do seu salário? "))
if salario > 1250:
    print(f"Seu aumento será de 10%, e o seu novo salário será de R${salario*1.1} reais.")
else:
    print(f"Seu aumento será de 15%, e o seu novo salário será de R${salario*1.15} reais.")
    
