from random import choice
numeros = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'
maior = menor = 0
print('Os valores sorteados foram:', end=' ')
for c in range(0, 5):
    v = choice(numeros)
    print(v, end=' ')
    if c == 0:
        maior = v
        menor = v
    else:
        if v > maior:
            maior = v
        if v < menor:
            menor = v
print(f'\nO maior valor sorteado foi {maior}\nO menor valor sorteado foi {menor}')
