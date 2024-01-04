print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termos = p + r*10       # termo geral de uma P.A (enésimo termo de uma P.A): ªn = ª1 + r*(n-1)
for c in range(p, termos, r):
    print(c, end=' → ')
print('ACABOU')
