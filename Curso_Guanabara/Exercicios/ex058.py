from random import randint

print(f'''{"-=-" * 10}
JOGO DA ADIVINHAÇAO
{"-=-" * 10}
''')

computador = randint(0,10)
cont = 0

jogador = int(input('Digite um numero de 0 a 10 e tente adivinhar o numero que o computador pensou: \n'))

while jogador != computador:
    cont += 1
    jogador = int(input('Você errou, tente novamente:\n '))

print(f'Voce acertou na {cont + 1} tentativa')
