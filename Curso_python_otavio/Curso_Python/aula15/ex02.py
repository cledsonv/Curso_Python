nome_usuario = str(input('Digite seu nome: '))
hora_atual = int(input('Informe a hora(0 - 23): '))

if hora_atual < 12:
    print(f'Bom dia {nome_usuario}')
elif hora_atual < 18:
    print(f'Boa tarde {nome_usuario}')
elif hora_atual < 24:
    print(f'Boa noite {nome_usuario}')
else:
    print('HORAS INVALIDAS...TENTE NOVAMENTE')