def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:.1f} x {comp:.1f} é de {a:.1f}m²')


print(f'Controle de Terrenos\n{"-"*20}')
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
