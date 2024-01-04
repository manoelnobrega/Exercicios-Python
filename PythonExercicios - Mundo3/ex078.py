numeros = []
for c in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a Posição {c}: ')))
maior = max(numeros)
menor = min(numeros)
print('=-'*30)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi o {maior} nas posições', end=' ')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi o {menor} nas posições', end=' ')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}... ', end='')
