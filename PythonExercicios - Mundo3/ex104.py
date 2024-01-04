def leiaInt(num):
    while True:
        n_def = str(input(num))
        if n_def.isnumeric():
            return n_def
        else:
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')


# Programa Principal
n_global = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n_global}')
