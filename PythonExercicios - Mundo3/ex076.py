itens = 'Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livro', \
    1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90
print('-'*42)
print('LISTAGEM DE PREÇOS'.center(42))
print('-'*42)
for c in range(0, len(itens)):
    if c == 8:
        break
    print(f'{itens[c]:.<33}R${itens[c + 9]:>7.2f}')
print('-'*42)