# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("Digite o nome de uma cidade: ")).strip().upper()
print(f"O nome da cidade começa com SANTO? {'SANTO' in cidade[0:5]}")
