print(f"""
{'-=-' * 7}
LOJAO BOM NO PREÇO 
{'-=-' * 7}
""")

soma = cont = preço = preço_menor = cont_preço = 0
nome_menor = ' '

while True:
    print('-=-' * 7)
    
    cont += 1
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    soma += preço

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N] ')).strip().upper()
    print('-=-' * 7)
    
    if preço > 1000:
        cont_preço += 1
    if cont == 1:
        preço_menor = preço
        nome_menor = nome
    else:
        if preço < preço_menor:
            nome_menor = nome
    if continuar == 'N':
        break

print(f'Valor total: {soma}')
print(f'{cont_preço} produtos custam mais de R$1000')
print(f'Nome do produto mais barato: {nome_menor}')