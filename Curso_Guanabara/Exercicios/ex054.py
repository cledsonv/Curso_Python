from datetime import date

cont1 = 0
cont2 = 0

for perg in range(1, 8):
    ano_atual = date.today().year
    ano = int(input(f'Em que ano a {perg} nasceu: '))

    if ano_atual - ano >= 21:
        cont1 += 1

    else:
        cont2 += 1

print(f'\nTem {cont2} pessoas menor de idade \nE {cont1} maiores de idade')