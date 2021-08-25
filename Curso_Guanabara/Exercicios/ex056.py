m = 0
velho = 0
mulher_menor = 0
nome_velho = ' '

for cadastro in range(1, 5):
    print(f'{"=" * 6} {cadastro} CADASTRO {"=" * 6}')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('M/F: ')).upper().strip()

    m += idade

    if cadastro == 1 and sexo == 'M':
        velho = idade
        nome_velho = nome
    if idade > velho and sexo == 'M':
        velho = idade
        nome_velho = nome
    if idade < 20 and sexo == 'F':
            mulher_menor += 1

media = m / 4

print(f'\nA media de idade do grupo é de {media}')
print(f'O homem mais velho é {nome_velho} com {velho} anos ')
print(f'{mulher_menor} mulheres tem menos de 20 anos')