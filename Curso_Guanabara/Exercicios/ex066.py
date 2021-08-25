cont = num = s = 0

while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    cont += 1
    s += num
print(f'Foi digitado {cont} numeros e a soma entre eles deu {s}')