cont = 0
soma = 0

for c in range(1, 501, 2):
   if c % 3 == 0:
       soma += c
       cont += 1
print(f'A soma de {cont} valores da {soma}')
print('Fim')