num = int(input('Digite um numero para ver o seu fatorial: '))
fac = 1

for c in range(num, 0, -1):
    fac *= c

print(f'O fatorial de {num} é {fac}')