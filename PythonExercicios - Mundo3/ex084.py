pessoas = list()
dados = list()
tot_pessoas = maiorP = menorP = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maiorP = menorP = dados[1]
    else:
        if dados[1] > maiorP:
            maiorP = dados[1]
        if dados[1] < menorP:
            menorP = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break
print('-='*30)
print(f'O total de pessoas registradas foi {len(pessoas)}')
print(f'O maior peso foi {maiorP}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maiorP:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi {menorP}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menorP:
        print(f'[{p[0]}]', end=' ')
