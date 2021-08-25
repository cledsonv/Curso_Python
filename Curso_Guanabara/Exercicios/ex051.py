
print(f"""{'-=-' * 10}
PRIMEIROS 10 TERMOS DE UM PA
{'-=-' * 10} 
""")

num = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))

s = num

print(end=f'{num}')

for pa in range(0, 9):
    s += razao
    print(end=f' => {s}')
print(end=' => Acabou')