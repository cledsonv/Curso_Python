print(f'''{"-=-" * 10}
SEQUENCIA DE FIBONACE
{"-=-" * 10}
''')


num = int(input('Digite um numero inteiro: '))

t1 = 0
t2 = 1
cont = 3

while cont <= num:
    t3 = t1 + t2
    print(f'{t3} > ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('Acabou')