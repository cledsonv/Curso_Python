peso = float(input('Digite seu peso(Kg): '))
altura = float(input('Digite a sua altura(m): '))

imc = peso / (altura ** 2)

print(f'O seu IMC é de {imc:.1f}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obsedade mormida')