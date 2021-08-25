num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if num1 > num2:
    print(f'{num1} é o Maior')
elif num2 > num1:
    print(f'{num2} é o Maior')
else:
    print('Os dois valores são iguais')