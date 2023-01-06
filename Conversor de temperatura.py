# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tcelsius = float(input("Digite o valor de uma temperatura, em graus Celsius: "))
tfahrenheit = ((tcelsius*9)/5) + 32
print(f"O valor de {tcelsius}°C vai equivaler a {tfahrenheit}°F.")
