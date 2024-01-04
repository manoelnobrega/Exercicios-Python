s = 0
cont = 0
for c in range(3, 501, 6):
    cont += 1
    s += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, s))
