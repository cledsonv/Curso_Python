print(f'''{"-=-" * 10}
OS 10 PRIMEIROS TERMOS DE UMA PA
{"-=-" * 10}
''')

num = int(input('Primeiro termo: '))
razao = int(input('Razao: '))

cont = 1
s = num
perg = 10
total = 0
cont2 = 1

while perg != 0:
    total += perg
    while cont <= total:
        print(f'{s} > ', end='')
        cont += 1
        s += razao
    print('Acabou')
    perg = int(input('Quantos termos quer mostrar a mais? '))
print(f'Mostrou a PA de {total} termos')
