# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o valor do seu salário? "))
anos = float(input("Em quantos anos será feito o pagamento? "))

if casa/(anos*12) <= salario*0.3:
    print("Parabéns, o empréstimo foi aprovado!")
else:
    print("O empréstimo foi negado.")
