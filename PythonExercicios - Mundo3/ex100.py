def sorteia():
    from random import randint
    from time import sleep
    numeros = list()
    print(f'Sorteando 5 valores da lista:', end=' ')
    while len(numeros) < 5:
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')

    def soma_par():
        total_par = 0
        for num in numeros:
            if num % 2 == 0:
                total_par += num
        print(f'Somando os valores pares de {numeros}, temos {total_par}')
    soma_par()


sorteia()
