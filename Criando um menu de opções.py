# Crie um programa que leia dois valores e mostre um menu na tela: 1-somar, 2-multiplicar, 3-maior, 4-novos números, 5-sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

opção = 0
while opção < 1 or opção > 5:
  print("\nO que você deseja fazer com esses dois números?\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa")
  opção = int(input("Resposta: "))
  if opção < 1 or opção > 5:
    print("\nOpção inválida, tente novamente.")
  if opção == 1:
    print(f"\nA soma entre {num1} e {num2} é igual a {num1+num2}")
  elif opção == 2:
      print(f"\nA multiplicação entre {num1} e {num2} é igual a {num1*num2}")
  elif opção == 3:
      if num1 > num2:
          print(f"O maior número entre {num1} e {num2} é {num1}.")
      else:
          print(f"O maior número entre {num1} e {num2} é {num2}.")
  elif opção == 4:
          num1 = int(input("\nDigite o primeiro número inteiro: "))
          num2 = int(input("Digite o segundo número inteiro: "))
          opção = 0
  elif opção == 5:
            print("\nVocê saiu do programa.")
