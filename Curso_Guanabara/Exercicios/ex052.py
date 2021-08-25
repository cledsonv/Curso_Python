num = int(input('Digite um numero inteiro: '))
contador = 0

for v in range(1, num + 1):

    if num % v == 0:
        print('\033[1;34m', end='')
        contador += 1
    else:
        print('\033[m', end='')

    print(v, end=' ')

print(f'\n\033[mO numero {num} foi divisivel {contador} vezes')

if contador == 2:
    print('\nELE E NUMERO PRIMO')
else:
    print('\nELE NAO E NUMERO PRIMO')