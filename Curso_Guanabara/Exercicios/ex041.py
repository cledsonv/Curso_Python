ano = int(input('Em que ano nasceu? '))

idade = 2021 - ano

if idade <= 9:
    print('SUA CAREGORIA É: MIRIM')
elif idade <= 14:
    print('SUA CATEGORIA É: INFANTIL')
elif idade <= 19:
    print('SUA CATEGORIA É: JUNIOR')
elif idade <= 25:
    print('SUA CATEGORIA É: SENIOR')
else:
    print('SUA CATEGORIA É: MASTER')