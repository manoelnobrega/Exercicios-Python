# Utilizando 'for' e fatorial sem import:
n = int(input('Digite um número para\ncalcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
for a in range(n, 0, -1):
    print('{}'.format(a), end='')
    print(' x ' if a > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
'''
# Utilizando 'while' usando 'math':
from math import factorial
n = int(input('Digite um número para\ncalcular seu Fatorial: '))
print('Calculando {}! = {}'.format(n, n), end=' ')
f = factorial(n)
while n > 1:
    n -= 1
    print('x {}'.format(n), end=' ')
print('= {}'.format(f))
'''
