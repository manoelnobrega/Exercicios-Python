numeros = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break
print('-='*30)
print(f'A lista completa é {numeros}\nA lista de pares é {pares}\nA lista de ímpares é {impares}')

'''RESOLUÇÃO GUANABARA:
numeros = list()
pares = list()
impares = list()
while True:
    numero.append(int(input('Digite um número: ')))
    opc = str(input('Quer continuar? [S/N] '))
    if opc in 'Nn':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*30)
print(f'A lista completa é {numeros}\nA lista de pares é {pares}\nA lista de ímpares é {impares}')
'''