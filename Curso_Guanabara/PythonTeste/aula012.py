name = str(input('What is your name? ')).title()

if name == 'Cledson':
    print('Iae gostoso')
elif name == 'Pedro' or name == 'Lucas' or name == 'Joao':
    print('Que nome cringe')
elif name in 'Juliana Claudia Raquel Leiticia':
    print('Hummmmmm cuie')
else:
    print('Nome normal')

print(f'Tenha um otimo dia {name}')