valor = float(input('Valor da Casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valor / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação mensal será de R${:.2f}'.format(valor, anos, prestacao))
if prestacao <= sal * 0.3:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

'''
print('Manoel de óculos azul ', end='')   ----> lembrar do end='' ao final de uma string para juntar à string de baixo
print('e boné cinza')

Manoel de óculos azul e cinza
'''
