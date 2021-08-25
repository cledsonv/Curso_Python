# for c in range(0, 6, 2):
#     print(c)
# print('Acabo')


# from time import sleep
# começo = int(input('Começo: '))
# fim = int(input('Final: '))
# passo = int(input('Passar de quanto em quanto? '))
#
# for c in range(começo, fim+1, passo):
#     sleep(1)
#     print(c)
# print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um numero: '))
    s += n
print(f'A soma dos valores deu {s}')