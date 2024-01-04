'''MINHA RESOLUÇÃO:
matriz = [[], [], [], [], [], [], [], [], []]
for c in range(0, 9):
    matriz[c].append(int(input('Digite um valor: ')))
print('-='*30)
for i, n in enumerate(matriz):
    print(f'{n}', end='')
    if i == 2 or i == 5:
        print()
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
