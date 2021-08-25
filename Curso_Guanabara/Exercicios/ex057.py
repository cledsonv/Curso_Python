sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite novamente: ')).upper()

print('Dados registrado com sucesso')