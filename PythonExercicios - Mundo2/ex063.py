# Fórmula da Sequência de Fibonacci:  Fn = Fn - 1 + Fn - 2
format = '-'*22
print('{}\nSEQUÊNCIA DE FIBONACCI\n{}'.format(format, format))
t = int(input('Quantos termos você quer mostrar? '))
cont = 0
n1 = -1
n2 = 1
print('~'*45)
while t > cont:
    cont += 1
    n3 = n1 + n2
    print('{} ->'.format(n3), end=' ')
    n1 = n2
    n2 = n3
print('FIM')
print('~'*45)
