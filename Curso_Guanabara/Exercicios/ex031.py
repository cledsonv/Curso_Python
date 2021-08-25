km = float(input('Quantos km voce pecorreu? '))

if km <= 200:
    print(f'Vocẽ vai pagar R${km * 0.50}')
else:
    print(f'Voce vai pagar R${km * 0.45}')