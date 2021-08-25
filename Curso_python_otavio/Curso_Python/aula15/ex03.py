usuario_nome = str(input('Digite o seu nome: '))
usuario_letras = len(usuario_nome)

if usuario_letras <= 4:
    print('Seu nome é curto')
elif usuario_letras <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')