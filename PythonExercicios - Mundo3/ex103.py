def ficha(nome='', gols=''):
    if gols.isnumeric():
        gols = int(g)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = input('Número de Gols: ')
ficha(n, g)