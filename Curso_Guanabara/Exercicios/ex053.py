frase = str(input('Digite uma frase: ')).lower().strip().split()

list = ''.join(frase)

if list[::-1] == list:
    print(f'A frase  é um polidramo')
else:
    print(f'A frase  não e um polidramo')