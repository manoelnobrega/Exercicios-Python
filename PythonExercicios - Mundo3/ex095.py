jogadores = list()
jogador = dict()
while True:
    jogador["nome"] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador["gols"] = list()
    for c in range(1, partidas + 1):
        jogador["gols"].append(int(input(f'Quantos gols na partida {c}? ')))
    total = 0
    for c in range(0, partidas):
        total += jogador["gols"][c]
    jogador["total"] = total
    jogadores.append(jogador.copy())
    opc = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while opc not in 'SN':
        print('ERRO! Digite apenas S ou N')
        opc = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if opc == 'N':
        break
print('-='*30)
print(f'cod', end=' ')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print(f'\n{"-"*40}')
for i, v in enumerate(jogadores):
    print(f'{i:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    print('-'*40)
    cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if cod < len(jogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"]}:')
        for i, g in enumerate(jogadores[cod]["gols"]):
            print(f'No jogo {i+1} fez {g} gols.')
    elif cod == 999:
        print('<< VOLTE SEMPRE >>')
        break
    else:
        print(f'ERRO! Não existe jogador com código {cod}!')
