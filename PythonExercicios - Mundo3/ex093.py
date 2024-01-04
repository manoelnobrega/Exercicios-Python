jogador = dict()
total = 0
jogador["nome"] = str(input('Nome do Jogador: ')).strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador["gols"] = list()
for c in range(1, partidas+1):
    jogador["gols"].append(int(input(f'Quantos gols na partida {c}? ')))
for c in range(0, partidas):
    total += jogador["gols"][c]
jogador["total"] = total
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, g in enumerate(jogador["gols"]):
    print(f'   => Na partida {i+1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
