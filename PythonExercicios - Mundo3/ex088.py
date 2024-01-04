from random import randint
from time import sleep
jogo = []
print('-'*30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-'*30)
j = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{"-="*5} SORTEANDO {j} JOGOS {"-="*5}')
for c in range(1, j+1):
    sleep(1)
    print(f'Jogo {c}:', end=' ')
    while len(jogo) != 6:
        r = randint(1, 60)
        jogo.append(r)
        jogo.sort()
        for x in range(0, len(jogo)):
            if jogo[x] == jogo[x-1]:
                jogo.pop(x)
                new_r = randint(1, 60)
                jogo.append(new_r)
                jogo.sort()
    print(jogo)
    jogo.clear()
sleep(1)
print(f'{"-="*6} < BOA SORTE! > {"-="*6}')
