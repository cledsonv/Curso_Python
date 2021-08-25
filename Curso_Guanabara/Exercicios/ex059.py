from time import sleep

resposta = 0
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

while resposta != 5:
    sleep(2)
    print(f'''{"-=-" * 10}
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos numeros
[5]Sair do progama
{"-=-" * 10}
''')
    resposta = int(input('>>>Qual opçao voce deseja? '))
    if resposta == 1:
        print(f'A soma de {num1} e {num2} é {num1 + num2}')
    if resposta == 2:
        print(f'O resultado de {num1} * {num2} = {num1 * num2}')
    if resposta == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        else:
            print(f'{num2} é maior que {num1}')
    if resposta == 4:
        num1 = int(input('Digite o primeiro valor novamente: '))
        num2 = int(input('Digite o segundo valor novamente: '))
    if resposta > 5 or resposta < 1:
        print('Valor errado, tente novamente ')
print('Progama finalizado...')