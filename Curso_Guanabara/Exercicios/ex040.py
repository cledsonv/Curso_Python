med1 = float(input('Digite a primeira nota: '))
med2 = float(input('Digite a segunda nota: '))

total = (med1 + med2) / 2

print(f'Média = {total}')

if total < 5:
    print('\033[1;31mREPROVADO\033[m')
elif total >= 5 and total < 7:
    print('\033[1;34mRECUPERAÇÃO\033[m')
elif total >= 7:
    print('\033[1;32mAPROVADO\033[m')