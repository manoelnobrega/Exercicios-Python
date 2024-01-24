def verificarTxt(n):
    try:
        a = open(n, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarTxt(n):
    try:
        a = open(n, 'wt+')
        a.close()
    except:
        print('\033[0;31mHouve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'\033[0;32mArquivo {n} criado com sucesso!\033[m')


def lerTxt(n):
    try:
        a = open(n, 'rt')
    except:
        print('\033[0;31mERRO ao ler o arquivo\033[m')
    else:
        print(a.read())
