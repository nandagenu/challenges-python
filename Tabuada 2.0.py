# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

number = int(input("Digite um número para calcular a tabuada: "))
print(f"\nTabuada do nº {number}:")
for i in range(1,10):
  print(f"{number}x{i} = {4*i}")
