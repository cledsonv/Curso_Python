from random import shuffle

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')

total = [nome1, nome2, nome3, nome4]
shuffle(total)

print('A ordem é: ')
print(total)