numeros = list()
while True:
    v = int(input('Digite um valor: '))
    if v in numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numeros.append(v)
        print('Valor adicionado com sucesso...')
    opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break
print('-='*30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
