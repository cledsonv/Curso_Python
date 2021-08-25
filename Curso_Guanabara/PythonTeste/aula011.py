# 30  black       preto          40
#
# 31  red           vermelho   41
#
# 32  green       verde         42
#
# 33  yellow      amarelo    43
#
# 34  blue      azul           44
#
# 35  Magenta  Magenta  45
#
# 36  cyan         ciano         46
#
# 37  grey          cinza         47
#
# 97  white        branco     107


nome = 'Cledson'
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m',
           }

print(f'Ola, {cores["vermelho"]}{nome}{cores["limpa"]} seja muito bem vindo')