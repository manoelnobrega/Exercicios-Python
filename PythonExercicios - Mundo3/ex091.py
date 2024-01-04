from time import sleep
from random import randint
jogadores = dict()
print('Valores sorteados:')
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)
    sleep(1)
    print(f'jogador{c} tirou {jogadores[f"jogador{c}"]} no dado.')
print('-='*30)
print(' == RANKING DOS JOGADORES ==')
for i, (k, v) in enumerate(sorted(jogadores.items(), key=lambda item: item[1], reverse=True)):
    print(f'{i+1}º lugar: {k} com {v}')
# Explicando esse último for: Primeiro eu dei enumerate para pegar o índice(i) e ficar mais fácil a formatação
# Depois eu dei um sorted nos items do dicionário 'jogadores', e dentro desse sorted eu coloquei argumentos como:
# O 'key=lambda item: item[1]' faz com que o sorted seja feito a partir dos valores(values) que os jogadores obtiveram.
# Se quiser fazer com as chaves(keys) ao invés dos valores, use item[0].
# RESOLUÇÃO DO GUANABARA:
# Na resolução dele ele usa o 'from operator import itemgetter' de forma que o itemgetter entre como argumento no sorted
# Ficaria assim: sorted(jogadores.items(), key=itemgetter(1), reverse=True) --> Aqui o itemgetter pega os values do dict
# Usando itemgetter(0) você pega as keys