def verificarTxt(path):
    try:
        a = open(path, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarTxt(path):
    try:
        a = open(path, 'wt+')
        a.close()
    except:
        print('\033[0;31mHouve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'\033[0;32mArquivo {path} criado com sucesso!\033[m')


def lerTxt(path):
    try:
        a = open(path, 'rt')
    except:
        print('\033[0;31mERRO ao ler o arquivo\033[m')
    else:
        txt = list(a.read())
        for i, dado in enumerate(txt):
            print(f'{txt[i]} /// {txt[i+1]}')


def escreverTxt(name, age, path):
    try:
        nome = str(input(name).strip())
        idade = int(input(age).strip())
    except (ValueError, TypeError):
        print('\033[0;31mERRO! Digite um nome e/ou idade válido(s)')
    else:
        a = open(path, 'a')
        a.writelines(nome, idade)
        a.close()
        print(f'Novo registro de {nome} adicionado.')
