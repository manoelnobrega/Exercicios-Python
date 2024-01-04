import moeda as m
valor = float(input('Digite o preço: R$'))
print(f'A metade de {m.moeda(valor)} é {m.moeda(m.metade(valor))}')
print(f'O dobro de {m.moeda(valor)} é {m.moeda(m.dobro(valor))}')
print(f'Aumentando 10%, temos {m.moeda(m.aumento(valor, 10))}')
