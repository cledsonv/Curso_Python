cont = s = 0
perg = ''

num = int(input('Digite um numero: '))

maior = menor = num

while perg != 'N':
    cont += 1
    s += num
    perg = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if perg == 'S':
        num = int(input('Digite um numero: '))
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f'A media dos valores foi {s / cont:.2f}')
print(f'O menor valor foi {menor} e o maior valor foi {maior}')