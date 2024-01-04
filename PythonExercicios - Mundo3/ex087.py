matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = terceira_coluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):                      # Esses dois primeiros 'for' leem o valor e aplicam na lista
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 12)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        # Exercício 87:
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            terceira_coluna += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c] > maior:
                    maior = matriz[l][c]        # Tudo isso poderia ser substitúido por: max(matriz[1])
    print()
print('-=' * 12)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terceira_coluna}.')
print(f'O maior valor da segunda linha é {maior}.')