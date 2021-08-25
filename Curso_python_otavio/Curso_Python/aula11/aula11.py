"""
Operadores relacionais
== > >= <= !=
"""

nome = str(input('Digite o seu nome: '))
idade = int(input('Digite sua idade: '))

idade_limite = 18

if idade >= idade_limite:
    print('Ja pode ficar devendo pro banco')
else:
    print('Se fudeu vai ter que pedir pro agiota')
