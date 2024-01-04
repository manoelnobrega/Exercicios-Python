from time import sleep
print('=-'*6, end='')
print(' \033[4;31;40mLOJA DO MAGRÃO\033[m ', end='')
print('-='*6)
preco = float(input('Preço das compras: \033[;32mR$ \033[m'))
sleep(1)
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista no cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
opcao = int(input('Digite sua opção: '))
sleep(1)
if opcao == 1:
    desc = preco * 0.90
    print('Sua compra de \033[;32mR$\033[m{:.2f} vai custar \033[;32mR$\033[m{:.2f} no final.'.format(preco, desc))
elif opcao == 2:
    desc = preco * 0.95
    print('Sua compra de \033[;32mR$\033[m{:.2f} vai custar \033[;32mR$\033[m{:.2f} no final.'.format(preco, desc))
elif opcao == 3:
    print('Sua compra de \033[;32mR$\033[m{:.2f} será parcelada em 2x de \033[;32mR$\033[m{:.2f} SEM JUROS.'
          .format(preco, preco/2))
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    preco_novo = preco * 1.20
    sleep(1.5)
    print('Sua compra será parcelada em {}x de \033[;32mR$\033[m{:.2f} COM JUROS'.format(parcela, preco_novo/parcela))
    print('Sua compra de \033[;32mR$\033[m{:.2f} vai custar \033[;32mR$\033[m{:.2f} no final.'
          .format(preco, preco_novo))
else:
    print('\033[0;31mERRO!!!\033[m\nOPÇÃO INVÁLIDA de pagamento! Tente novamente.')
