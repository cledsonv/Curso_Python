from time import sleep

print(f"""{'-=-' * 10}
\033[31m APROVAMENTO DE EMPRESTIMO\033[m
{'-=-' * 10}
""")

casa = float(input('Qual é o valor da casa: R$'))
salario = float(input('Quanto vocẽ recebe? R$'))
anos = int(input('Em quantos anos voce que pagar? '))

prestaçao = casa / (anos * 12)

if (salario * 0.3) < prestaçao:
    print('EMPRESTIMO REPROVADO')
else:
    print('\033[31mAPROVADO...\033[m')
    sleep(2)
    print(f'Vocẽ vai pagar em torno de \033[1;32mR${prestaçao:.2f}\033[m ao mẽs')