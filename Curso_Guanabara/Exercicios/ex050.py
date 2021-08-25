s = 0
for c in range(0, 4):
    num = int(input('Digite um numero inteiro: '))
    if (num % 2) == 0:
        s += num
print(f'A soma dos valores pares foi {s}')
