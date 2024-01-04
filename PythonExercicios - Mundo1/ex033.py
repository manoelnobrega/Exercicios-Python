a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# descobrindo o menor valor
if a < b:
    if a < c:
        print('O menor valor digitado foi {}'.format(a))
    else:
        print('O menor valor digitado foi {}'.format(c))
else:
    if b < c:
        print('O menor valor digitado foi {}'.format(b))
    else:
        print('O menor valor digitado foi {}'.format(c))
# descobrindo o maior valor:
if a > b:
    if a > c:
        print('O maior valor digitado foi {}'.format(a))
    else:
        print('O maior valor digitado foi {}'.format(c))
else:
    if b > c:
        print('O maior valor digitado foi {}'.format(b))
    else:
        print('O maior valor digitado foi {}'.format(c))
