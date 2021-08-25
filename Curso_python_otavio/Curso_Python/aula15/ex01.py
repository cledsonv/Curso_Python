num_usuario = input('Digite um número: ')

if num_usuario.isdigit():
    num_usuario = int(num_usuario)

    if (num_usuario % 2) == 0:
        print(f'O número {num_usuario} é par')
    else:
        print(f'O número {num_usuario} é impar')
else:
    print('Não é um número inteiro, por favor renicie o progama e tente novamente')