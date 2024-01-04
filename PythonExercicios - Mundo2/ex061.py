# termo geral de uma P.A (enésimo termo de uma P.A): ªn = ª1 + r*(n-1)
print('Gerador de PA\n{}'.format('-='*8))
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
n = p + r*9     # 10º termo da PA
print(p, end=' -> ')
while p != n:
    p += r
    print('{} -> '.format(p), end='')
print('FIM')
