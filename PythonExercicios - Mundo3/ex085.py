numeros = list()
numeros.append(list())
numeros.append(list())
for c in range(1, 8):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('-='*30)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numeros[1])}')
