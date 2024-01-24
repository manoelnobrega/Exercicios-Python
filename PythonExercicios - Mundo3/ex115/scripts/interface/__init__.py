from time import sleep
from arquivo import *

def menu(msg):
    cores = {
        'verde': '\033[0;32m',
        'amarelo': '\033[0;33m',
        'azul': '\033[0;34m',
        'vermelho': '\033[0;31m',
        'fechar': '\033[m'}
    while True:
        print('-'*30)
        print(f'{cores["verde"]}{"Menu Principal":^28}{cores["fechar"]}')
        print('-'*30)
        print(f'{cores["amarelo"]}1{cores["fechar"]} - {cores["azul"]}Ver pessoas cadastradas{cores["fechar"]}')
        print(f'{cores["amarelo"]}2{cores["fechar"]} - {cores["azul"]}Cadastrar nova pessoa{cores["fechar"]}')
        print(f'{cores["amarelo"]}3{cores["fechar"]} - {cores["azul"]}Sair do sistema{cores["fechar"]}')
        print('-'*30)
        opc = 0
        while True:
            try:
                opc = int(input(f'{cores["amarelo"]}{msg}{cores["fechar"]}').strip()[0])
            except (ValueError, TypeError, IndexError):
                print(f'{cores["vermelho"]}ERRO! digite um número inteiro válido!{cores["fechar"]}')
                continue
            else:
                if opc == 1:
                    arq = 'cadastros.txt'
                    if not verificarTxt(arq):
                        criarTxt(arq)
                    sleep(1)
                    print('-'*30)
                    print(f'{"PESSOAS CADASTRADAS":^28}')
                    print('-'*30)
                    lerTxt(arq)
                    sleep(1)
                    break
                elif opc == 2:
                    sleep(1)
                    print('-'*30)
                    print(f'{"Opção 2":^28}')
                    print('-'*30)
                    sleep(1)
                    break
                elif opc == 3:
                    print('-'*30)
                    print(f'{"Saindo do sistema... Até logo!":^28}')
                    print('-'*30)
                    sleep(1.5)
                    break
                else:
                    print(f'{cores["vermelho"]}ERRO! digite uma opção válida!{cores["fechar"]}')
                    continue
        if opc == 3:
            break
        else:
            continue
