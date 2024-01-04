def numeros(* valores):
    from time import sleep
    print('-='*20)
    print('Analisando os valores passados...')
    cont = maior = 0
    for num in valores:
        print(f'{num}', end=' ')
        if cont == 0:
            maior = num
        else:
            if maior < num:
                maior = num
        cont += 1
        sleep(0.4)
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


numeros(2, 9, 4, 5, 7, 1)
numeros(4, 7, 0)
numeros(1, 2)
numeros(6)
numeros()