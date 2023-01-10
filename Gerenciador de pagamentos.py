#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

value = float(input("Qual o preço do produto? "))
pgto = int(input("Qual a forma de pagamento?\nDigite 1 para À VISTA NO CARTÃO\n2 para À VISTA DINHEIRO/CHEQUE\n3 para EM ATÉ 2X NO CARTÃO\n4 para 3X OU MAIS NO CARTÃO\nResposta: "))

if pgto == 1:
    print(f"O valor do produto com 10% de desconto ficará em R${value*0.9} reais.")
elif pgto == 2:
    print(f"O valor do produto com 5% de desconto ficará em R${value*0.95} reais.")
elif pgto == 3:
    print(f"O valor do produto com preço formal continuará em R${value} reais.")
elif pgto == 4:
    print(f"O valor do produto com 20% de juros ficará em R${value*1.2} reais ao mês.")
else:
    print("Opção inválida, tente novamente.")
