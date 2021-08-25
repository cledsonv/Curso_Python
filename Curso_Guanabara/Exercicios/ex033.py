n1 = int(input('Write one number: '))
n2 = int(input('Write other number: '))
n3 = int(input('Write other number again: '))

# if n1 > n2 > n3:
#     print(f'Maior: {n1}\nMenor: {n3}')
# if n1 > n3 > n2:
#     print(f'Maior: {n1}\nMenor: {n2}')
# if n2 > n1 > n3:
#     print(f'Maior: {n2}\nMenor: {n3}')
# if n2 > n3 > n1:
#     print(f'Maior: {n2}\nMenor: {n1}')
# if n3 > n2 > n1:
#     print(f'Maior: {n3}\nMenor: {n1}')
# if n3 > n1 > n2:
#     print(f'Maior: {n3}\nMenor: {n2}')

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'Menor: {menor}')
print(f'Maior: {maior}')