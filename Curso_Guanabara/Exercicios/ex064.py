cont = -1
perg = soma = 0


while perg != 999:
    cont += 1
    soma += perg
    perg = int(input('Digite um número [999 para parar]: '))
print(f'Foram digitados {cont} numeros e a soma deles deu {soma}')
