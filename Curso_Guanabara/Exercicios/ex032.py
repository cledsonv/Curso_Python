from datetime import date
years = int(input('What is the year, Coloque 0 para analisar o ano atual '))

if years == 0:
    years = date.today().year
if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
    print('Ele e bissexto')
else:
    print('Ele nao e bissexto')