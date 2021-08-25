cidade = str(input('Que cidade voce mora? '))

print(f'Ela tem Santos? {"santo" in cidade[:5].lower().strip()}')