print(f'''{"-=-" * 10}
10 PRIMEIROS TERMOS DE UMA PA
{"-=-" * 10}
''')

num = int(input('Digite um valor: '))
razao = int(input('Razao: '))

cont = 0
s = num

while cont != 10:
    print(f'{s} > ', end='')
    cont += 1
    s += razao

print('Acabou')