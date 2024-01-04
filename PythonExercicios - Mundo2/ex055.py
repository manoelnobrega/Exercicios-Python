maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg\nO menor peso lido foi de {}kg'.format(maior, menor))

# Também é possível fazer esse exercício usando 'max' e 'min' para ler o maior e o menor valor

'''
lista = []    
    lista.append(peso)
# Descobrindo o maior peso:
if lista[0] >= lista[1] and lista[0] >= lista[2] and lista[0] >= lista[3] and lista[0] >= lista[4]:
    maior = lista[0]
if lista[1] >= lista[0] and lista[1] >= lista[2] and lista[1] >= lista[3] and lista[1] >= lista[4]:
    maior = lista[1]
if lista[2] >= lista[0] and lista[2] >= lista[1] and lista[2] >= lista[3] and lista[2] >= lista[4]:
    maior = lista[2]
if lista[3] >= lista[0] and lista[3] >= lista[1] and lista[3] >= lista[2] and lista[3] >= lista[4]:
    maior = lista[3]
if lista[4] >= lista[0] and lista[4] >= lista[1] and lista[4] >= lista[2] and lista[4] >= lista[3]:
    maior = lista[4]
# Descobrindo o menor peso:
if lista[0] <= lista[1] and lista[0] <= lista[2] and lista[0] <= lista[3] and lista[0] <= lista[4]:
    menor = lista[0]
if lista[1] <= lista[0] and lista[1] <= lista[2] and lista[1] <= lista[3] and lista[1] <= lista[4]:
    menor = lista[1]
if lista[2] <= lista[0] and lista[2] <= lista[1] and lista[2] <= lista[3] and lista[2] <= lista[4]:
    menor = lista[2]
if lista[3] <= lista[0] and lista[3] <= lista[1] and lista[3] <= lista[2] and lista[3] <= lista[4]:
    menor = lista[3]
if lista[4] <= lista[0] and lista[4] <= lista[1] and lista[4] <= lista[2] and lista[4] <= lista[3]:
    menor = lista[4]
print('O maior peso lido foi de {}kg\nO menor peso lido foi de {}kg'.format(maior, menor))
'''
