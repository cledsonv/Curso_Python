from random import randint

print(f"""
{'-=-' * 5}
PAR OU IMPAR?
{'-=-' * 5}
""")

cont = total = 0


while True:
    computador = randint(1,10)
    jogador = int(input('Digite um numero: '))
    par_or_impar = str(input('Par ou Impar?(P/I) ')).upper()

    total = jogador + computador
    print('-=-' * 5)
    
    if par_or_impar == 'P' and total % 2 == 0:
        print('YOU WON...')
        print(f'O JOGADOR JOGOU {jogador} E O COMPUTADOR JOGOU {computador}. TOTAL DE {total} É IGUAL A PAR')
    if par_or_impar == 'P' and total % 2 == 1:
        print('YOU LOST...')
        print(f'O JOGADOR JOGOU {jogador} E O COMPUTADOR JOGOU {computador}. TOTAL DE {total} É IGUAL A IMPAR')
        break
    if par_or_impar == 'I' and total % 2 == 0:
        print('YOU LOST...')
        print(f'O JOGADOR JOGOU {jogador} E O COMPUTADOR JOGOU {computador}. O TOTAL DE {total} É IGUAL A PAR')
        break
    if par_or_impar == 'I' and total % 2 == 1:
        print('YOU WON...')
        print(f'O JOGADOR JOGOU {jogador} E O COMPUTADOR JOGOU {computador}. O TOTAL DE {total} É IGUAL A IMPAR')
    
    cont += 1
    print('-=-' * 5)
print('-=-' * 5)
print(f'YOU LOST OTARIO. VOCE VENCEU {cont} JOGADAS')