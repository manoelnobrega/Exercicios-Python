print('Gerador de PA\n{}'.format('-='*8))
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
n = p + r*9     # 10º termo da PA
print(p, end=' -> ')
while p != n:
    p += r
    print('{} -> '.format(p), end='')
print('PAUSA')
p2 = 1
cont = 0
while p2 != 0:
    p2 = int(input('Quantos termos você quer mostrar a mais? '))
    cont += p2
    n2 = n + (r * p2)
    while n != n2:
        n += r
        print('{} -> '.format(n), end='')
    if p2 != 0:
        print('PAUSA')
print('Progressão finalizada com {} termos mostrados.'.format(cont+10))
