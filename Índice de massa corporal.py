#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

peso = float(input("Qual o seu peso, em kg? "))
altura = float(input("Qual a sua altura, em metros? "))
imc = peso/altura**2

if imc < 18.5:
    print(f"Seu IMC é de {imc:.2f}, e você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print(f"Seu IMC é de {imc:.2f}, e você está no peso ideal.")
elif 25 <= imc < 30:
    print(f"Seu IMC é de {imc:.2f}, e você está com sobrepeso.")
elif 30 <= imc < 40:
    print(f"Seu IMC é de {imc:.2f}, e você está com obesidade.")
else:
    print(f"Seu IMC é de {imc:.2f}, e você está com obesidade mórbida.")
