# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Digite a largura da parede, em metros: "))
altura = float(input("Digite a altura da parede, em metros: "))
area = largura*altura
print(f"A quantidade de tinta necessária para pintar a parede de {area}m² será de {area/2} litros.")
