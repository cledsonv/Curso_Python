r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Triangulo Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Triangulo Escaleno')
    else:
        print('Triangulo Isoceles')
else:
    print('Não é um triângulo')