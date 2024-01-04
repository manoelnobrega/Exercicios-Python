lar = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))
area = lar * alt
print('Sua parede tem a dimensão {}x{} e sua área é de {}m².'.format(lar, alt, area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(area/2))
