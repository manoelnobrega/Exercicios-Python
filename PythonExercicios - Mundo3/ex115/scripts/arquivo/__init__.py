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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<22}{dado[1]:>3} anos')
    finally:
        a.close()


def escreverTxt(name, age, path):
    try:
        a = open(path, 'at')
        nome = str(input(name).strip())
        idade = int(input(age).strip())
    except (ValueError, TypeError):
        print('\033[0;31mERRO! Digite um nome e/ou idade válido(s)\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[0;31mHouve um ERRO ao escrever os dados do cadastro!\033[m')
        else:
            print(f'\033[0;32mNovo registro de {nome} adicionado.\033[m')
            a.close()
