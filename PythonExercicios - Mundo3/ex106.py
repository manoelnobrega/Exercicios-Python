def cores(frase, num=0, center=True):
    if center:
        if num == 1:
            verde_cent = print(f'\033[0;30;42m{frase:^30}\033[m')
            return verde_cent
        if num == 2:
            azul_cent = print(f'\033[0;30;44m{frase:^30}\033[m')
            return azul_cent


def resp(com):
    msg = help(com)
    return msg


while True:
    print('\033[0;30;42m~\033[m'*30)
    cores('SISTEMA DE AJUDA PyHELP', num=1)
    print('\033[0;30;42m~\033[m'*30)
    opc = str(input('Função ou Biblioteca > ').strip().lower())
    if opc == 'fim':
        break
    print('\033[0;30;44m~\033[m'*42)
    cores(f"Acessando o manual do comando '{opc}'", num=2)
    print('\033[0;30;44m~\033[m'*42)
    resp(opc)
