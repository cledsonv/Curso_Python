m = int(input('Digite o valor em \033[1mMetros:\033[m '))

km = m / 1000
hm = m /100
dam = m / 10
dm = m * 10
c = m * 100
mm = m * 1000

print(f'A medida de {m} metros corresponde: ')
print(f'{km}km \n{hm}hm \n{dam}dam')
print(f'{dm}dm \n{c}cm \n{mm}mm')