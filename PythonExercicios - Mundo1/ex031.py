km = float(input('Qual é a distância da sua viagem em quilômetros(km)? '))
preco1 = km * 0.5
preco2 = km * 0.45
print('Você está prestes a começar uma viagem de {:.1f}km.'.format(km))
if km <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(preco1))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(preco2))

# preco = km * 0.5 if km <= 200 else km * 0.45