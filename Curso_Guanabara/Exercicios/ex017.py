from math import hypot

cateto_oposto = float(input('Informe o cateto oposto: '))
cateto_adjacente = float(input('Informe o cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'O comprimento da hipotenusa é de {hipotenusa:.2f}')