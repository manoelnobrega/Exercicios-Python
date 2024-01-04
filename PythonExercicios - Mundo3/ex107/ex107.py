import moeda as m
valor = float(input('Digite o preço: R$'))
print(f'A metade de R${valor:.1f} é R${m.metade(valor):.1f}')
print(f'O dobro de R${valor:.1f} é R${m.dobro(valor):.1f}')
print(f'Aumentando 10%, temos R${m.aumento(valor, 10):.1f}')
