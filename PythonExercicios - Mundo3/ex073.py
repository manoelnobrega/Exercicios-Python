times = 'Palmeiras', 'Botafogo', 'Fluminense', 'Athletico-PR', 'Cruzeiro', 'Fortaleza', 'São Paulo', 'Atlético-MG',\
    'Santos', 'Grêmio', 'Internacional', 'Flamengo', 'Bahia', 'Bragantino', 'Vasco', 'Corinthians',\
    'Cuiabá', 'Goiás', 'América-MG', 'Coritiba'
print('-='*25)
print(f'Lista de Times do Brasileirão 2023 (5ª Rodada): {times}')
print('-='*25)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*25)
print(f'Os 4 últimos são: {times[16:]}')
print('-='*25)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*25)
print(f'O Vasco está na {times.index("Vasco")+1}ª posição')
print('-='*25)
print(f'O melhor time do mundo é São Paulo e ele está na {times.index("São Paulo")+1}ª posição')
