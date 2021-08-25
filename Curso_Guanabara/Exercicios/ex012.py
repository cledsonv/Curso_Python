preço = float(input('Digite o preço: '))
desc = preço * 0.95

print(f'O produto custara R${desc:.2f} com 5% de desconto ')
print(f'Desconto de -{preço - desc:.2f}')