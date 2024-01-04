import random
from time import sleep
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 19)
n = random.randint(0, 5)
n1 = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if n == n1:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(n, n1))
