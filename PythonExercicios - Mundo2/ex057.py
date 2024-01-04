sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]         # --> o [0] pega só a primeira letra da string
while sexo != 'M' and sexo != 'F':        # Poderia ser: while sexo not in 'MmFf':
    sexo = str(input('\033[1;31mDADOS INVÁLIDOS!\033[m Por favor, informe seu sexo: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
