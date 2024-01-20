def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print(f'\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except:
            print(f'\033[0;31mERRO: por favor, digite um número real válido.\033[m')
        else:
            return num


inteiro = leiaInt('Digite um Inteiro: ')
real = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}.')
