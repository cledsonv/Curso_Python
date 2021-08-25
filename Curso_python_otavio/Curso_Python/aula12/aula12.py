"""
and, or, not
not, not in
"""

usuario = str(input('Digite o nome de usuario '))
senha = str(input('Digite uma senha '))

usuario_log = 'cledson'
senha_log = '123456'

if usuario == usuario_log and senha == senha_log:
    print('Esse usuario ja esta logado ')
else:
    print('Usuario ou senha invalido ')