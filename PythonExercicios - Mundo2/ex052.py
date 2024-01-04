n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c != 0:
        print('\033[0;31m{}\033[m'.format(c), end=' ')   # vermelho
    else:
        print('\033[1;33m{}\033[m'.format(c), end=' ')   # amarelo
        cont += 1
if n == 0:
    print('O número 0 não pode ser divido')
else:
    print('\nO número {} foi divisível {} vezes'.format(n, cont))
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
