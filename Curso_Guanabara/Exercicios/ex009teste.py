from time import sleep
num = int(input('Digite um numero:'))
x = 1

while x <= 10:
    print('\033[1;31mCARREGANDO...\033[m')
    sleep(2)
    print(f'Taboada de {num}')
    print(f'{num} x {x} = {num * x}')
    x += 1
    if x == 11:
        print('\033[41mTabuada concluida\033[m')