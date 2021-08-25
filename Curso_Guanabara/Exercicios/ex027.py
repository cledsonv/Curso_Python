name = str(input('What is your name? ')).strip()
first = name.split(" ", 1)
last = name.rsplit(" ", 1)

print(f'Firt name: {"".join(first[0])}')
print(f'Last name: {"".join(last[1])}')
