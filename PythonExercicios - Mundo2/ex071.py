print('='*29)
print('BANCO CEV'.center(29))
print('='*29)
valor = int(input('Que valor você quer sacar? R$'))
cedulas = [50, 20, 10, 1]
valor_restante = 0
for c in range(0, 4):
    if valor - valor_restante > cedulas[c]:
        print(f'Total de {(valor - valor_restante) // cedulas[c]} cédulas de R${cedulas[c]}')
        valor_restante = (valor // cedulas[c]) * cedulas[c]
print('='*29)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
