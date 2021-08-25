frase = str(input('Digite uma frase: ')).strip().lower()

print(f'Existem {frase.count("a")} A')
print(f'Ela aparece na primeira vez na posiçao: {frase.find("a")+1}')
print(f'Ela aparece pela ultima vez na posiçao: {frase.rfind("a")+1}')