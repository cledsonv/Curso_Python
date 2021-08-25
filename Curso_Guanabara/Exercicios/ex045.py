from random import randint
from time import sleep

print("""
[0]Pedra
[1]Papel
[2]Tesoura
""")
escolha = int(input('Qual a sua jogada? '))
itens = ['Pedra', 'Papel', 'Tesoura']
comp = randint(0, 2)

print('PEDRA')
sleep(1)
print('PAPEEELLLLL')
sleep(1)
print('TESOUUUUURAAAAAA!!!!\n')

if escolha != 0 and escolha != 1 and escolha != 2:
    print('Numero errado, tente novamente')

else:
    print(f'Computador escolheu: {itens[comp]}')
    print(f'Jogador escolher: {itens[escolha]}')
    if comp == escolha:
        print('EMPATE')

    elif comp == 0:
        if escolha == 1:
            print('JOGADOR GANHA')

        elif escolha == 2:
            print('JOGADOR PERDE')

    elif comp == 1:
        if escolha == 0:
            print('COMPUTADOR GANHA')
        elif escolha == 2:
            print('JOGADOR GANHA')
    elif comp == 2:
        if escolha == 0:
            print('JOGADOR GANHA')
        elif escolha == 1:
            print('COMPUTADOR GANHA')