from random import choice

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')

total = [nome1, nome2, nome3, nome4]
sorteio = choice(total)

print(f'A pessoa escolhida é {sorteio}')
