from datetime import date

print(f"""
{'-=-' * 5}
ALISTAMENTO
{'-=-' * 5}
""")
sexo = int(input('''DIGITE
[1]Masculino
[2]Feminino
'''))

if sexo == 1:

    ano1 = int(input('Em que ano você nasceu? '))
    ano2 = date.today().year
    idade = ano2 - ano1

    if idade < 18:
        print(f'Falta {18 - idade} anos para voce capinar mato')
        print(f'Seu alistamento vai ser em {ano1 + 18}')
    elif idade > 18:
        print(f'Voce ja \033[4;31mPASSOU DO TEMPO\033[m em {idade - 18} anos')
        print(f'Seu alistamento foi em {ano1 + 18}')
    elif idade == 18:
        print(f'Vai capinar mato garotão!!!, ja esta na hora de se alistar')

elif sexo == 2:
    print('Você não prescisa se ALISTAR')