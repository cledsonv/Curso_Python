num = cont = 0
print(f"""{'-=-' * 10}
TABUADINHA DO GRAU
{'-=-' * 10}
""")

num = int(input('Que ver a tabuada até 10 de que valor? '))

while True:
    print(f'{"-=-" * 7}')

    while cont <= 10:
        print(f'{num} x {cont} = {num * cont}')
        cont += 1

    print(f"{'-=-' * 7}")
    cont = 0
    num = int(input('Que ver a tabuada até 10 de que valor? '))

    if num < 0:
        break

print('TABUADA FINALIZADA...')
