i = 0
prod_barato = []
while True:
    produto = str(input('Nome do Produto: ')).strip().capitalize()
    valor = float(input('Preço: R$'))
    prod_barato += [produto, valor]
    i += 1
    if i == 3:
        break
mais_barato = min(prod_barato)
print(f'{prod_barato} custa {mais_barato}')
    # print(f'O produto mais barato foi {prod_barato[0]} que custa R${prod_barato[1]:.2f}')