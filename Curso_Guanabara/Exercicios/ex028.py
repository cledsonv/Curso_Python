from random import randrange
from time import sleep

print(f"""
{'-=-' * 10}
\033[1;31mJOGO DA ADIVINHAÇÃO0\033[m
{'-=-' * 10}
""")

num = int(input('Digite um numero de 0 a 5 e tente adivinhar qual numero o computador pensou:\n'))
comp = randrange(6)
print('PROCESSANDO...')
sleep(2)
print(f'O numero escolhido foi {comp}')

if comp == num:
    print('VOCE GANHOU!!!')
else:
    print(f'{"-=-" * 15}\033[1;31m\nÇ   FIM DE JOGO, TENTE NOVAMENTE DEPOIS\033[m\n{"-=-" * 15}')