produto = float(input('INSIRA O VALOR: '))

print(f"""{'-=-' * 10}
[1]À VISTA DINHEIRO (10% DE DESCONTO)
[2]À VISTA CARTÃO ( 5% DE DESCONTO)
[3]ATÉ 2x NO CARTÃO ( PREÇO NORMAL )
[4]3x OU MAIS NO CARTÃO ( 20% DE JUROS )
{'-=-' * 10}
""")
pagamento = int(input('Digite a opçao desejada: '))
if pagamento == 1:
    print(f'PAGAMENTO: R${produto * 0.90:.2f}')
elif pagamento == 2:
    print(f'PAGAMENTO: R${produto * 0.95:.2f}')
elif pagamento == 3:
    print(f'PAGAMENTO: {produto}')
elif pagamento == 4:
    parcela = int(input('Quantas parcelas? '))
    print(f'''Sua compra sera parcelada em {parcela}x de R${(produto * 1.20) / parcela:.2f}
Que no total vai ficar: R${produto * 1.20}''')