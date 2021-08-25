num1 = int(input('Digite um numero inteiro: '))

num2 = int(input(f"""DIGITE
{"-=-" * 5}
[1] PARA BINÁRIO
[2] PARA OCTAL
[3] PARA HEXADECIMAL
{'-=-' * 5}
"""))

if num2 == 1:
    print(bin(num1)[2:])
elif num2 == 2:
    print(oct(num1)[2:])
elif num2 == 3:
    print(hex(num1)[2:])
else:
    print('Opçao invalida')