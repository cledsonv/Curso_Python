print(f'''
{'-=-' * 5}
CADASTRAMENTO
{'-=-' * 5}
''')

idade_maior = s = homem = mulher_menor = 0

while True:
    idade = int(input('Idade: ')) 
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    print('-=-' * 5)
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    
    if idade >= 18:
        idade_maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher_menor = 1
    print('-=-' * 5)
    if continuar == 'N':
        break

print(f'Tem {idade_maior} pessoas maiores de 18 anos')
print(f'Foram cadastrados {homem} homens')
print(f'Tem {mulher_menor} mulheres com menos de 20 anos')