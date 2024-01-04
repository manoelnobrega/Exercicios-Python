from random import randint
design = {'linhas_coloridas': '\033[1;32m=-\033[m'*13,
          'par': '\033[1;33mPAR\033[m',
          'impar': '\033[1;31mÍMPAR\033[m',
          }
print(f'{design["linhas_coloridas"]}')
print(f'VAMOS JOGAR {design["par"]} OU {design["impar"]}')
print(f'{design["linhas_coloridas"]}')
par = design["par"]
impar = design["impar"]
vitorias = 0
while True:
    num = int(input('Digite um valor: '))
    opc = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-'*26)
    comp = randint(0, 10)
    soma = num + comp
    print(f'Você jogou {num} e o computador {comp}.', end=' ')
    print(f'Total de {soma} deu {par}' if soma % 2 == 0 else f'Total de {soma} deu {impar}')
    print('-' * 26)
    if opc in 'Pp':
        opc = par
    elif opc in 'IiÍí':
        opc = impar
    else:
        print('\033[1;31mERRO!\033[m\nOPÇÃO INVÁLIDA: Escolha entre Par(P) ou Ímpar(I)\nTente novamente...')
        break
    if soma % 2 == 0:
        soma = par
    else:
        soma = impar
    if soma == opc:
        vitorias += 1
        print(f'Você VENCEU!\nVamos jogar novamente...\n', end=f'{design["linhas_coloridas"]}\n')
    else:
        print('Você PERDEU!\n', end=f'{design["linhas_coloridas"]}\n')
        print(f'GAME OVER! Você venceu {vitorias} vezes')
        break
