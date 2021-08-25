r1 = float(input('Digite o comprimento da reta1: '))
r2 = float(input('Digite o comprimento da reta2: '))
r3 = float(input('Digite o comprimento da reta2: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('This is triangle')

else:
    print('this is not triangle')