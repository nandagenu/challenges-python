# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes
# aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase qualquer: ")).strip().upper()

print(f"Quantas vezes aparece a letra 'A'? {frase.count('A')}")
print(f"Em que posição a letra 'A' aparece a primeira vez? {frase.find('A')}")
print(f"Em que posição a letra 'A' aparece a última vez? {frase.rfind('A')}")
