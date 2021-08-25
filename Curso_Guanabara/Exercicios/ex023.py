# n = int(input('Digite um número entre 0 e 9999: '))
# n2 = str(int(10000 + n))
# print(f'O número {n} possui, {n2[1]} milhares.')
# print(f'O número {n} possui, {n2[2]} centenas. ')
# print(f'O número {n} possui, {n2[3]} dezenas. ')
# print(f'O número {n} possui, {n2[4]} unidades.')

num = int(input('Digite um numero de 0 a 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')