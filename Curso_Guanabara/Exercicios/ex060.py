# from math import factorial
# n = int(input('Digite um numero para calcular o seu factorial: '))
# f = factorial(n)
# print(f'O factorial de {n} e igual a {f}.')

num = int(input('Digite um numero para calcular o seu factorial: '))
cont = num
fac = 1

print(f'Calculando {num}! = ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fac *= cont
    cont -= 1
print(fac)