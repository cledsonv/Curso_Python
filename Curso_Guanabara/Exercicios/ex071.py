print(f'''
{"-=-" * 5}
BANQUINHO DO JUNIOR
{"-=-" * 5}
''')

valor_sacado = int(input('Qual é o valor a ser sacado? R$'))

cedula50 = valor_sacado // 50
calc50 = valor_sacado % 50
cedula20 = calc50 // 20
calc20 = calc50 % 20
cedula10 = calc20 // 10
calc10 = calc20 % 10
cedula1 = calc10 // 1

print(f'Total de {cedula50} cedulas de R$50')
print(f'Total de {cedula20} cedulas de R$20')
print(f'Total de {cedula10} cedulas de R$10')
print(f'Total de {cedula1} cedulas de R$1')