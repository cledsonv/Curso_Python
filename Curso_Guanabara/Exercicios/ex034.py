salary = float(input('Enter your salary: R$'))

if salary <= 1250:
    print(f'Seu salario ficou R${salary * 1.15:.2f} com um aumento de 15%')
else:
    print(f'Seu salario ficou R${salary * 1.10:.2f} com um aumento de 10%')