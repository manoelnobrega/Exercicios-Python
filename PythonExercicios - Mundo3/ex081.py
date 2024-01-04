numeros = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break
print('-='*30)
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
print('O valor 5 faz parte da lista!'if 5 in numeros else 'O valor 5 não foi encontrado na lista!')
