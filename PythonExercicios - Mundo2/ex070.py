print('-'*28)
print('LOJA SUPER BARATÃO'.center(28))
print('-'*28)
tot_compra = tot_prod_caros = menor_valor = i = 0
prod_barato = ''
while True:
    i += 1
    produto = str(input('Nome do Produto: ')).strip().capitalize()
    valor = float(input('Preço: R$'))
    # Somando as compras:
    tot_compra += valor
    # Verificando produtos caros(>R$1000):
    if valor > 1000:
        tot_prod_caros += 1
    # Verificando o produto mais barato:
    if i == 1:
        menor_valor = valor
        prod_barato = produto
    else:
        if valor < menor_valor:
            menor_valor = valor
            prod_barato = produto
    opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opc not in 'SNÑ':
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opc in 'NÑ':
        break
print('-'*28)
print(f'O total da compra foi R${tot_compra:.2f}')
print(f'Temos {tot_prod_caros} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prod_barato} que custa R${menor_valor:.2f}')
