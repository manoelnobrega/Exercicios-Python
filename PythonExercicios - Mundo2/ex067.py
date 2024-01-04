while True:
    cont = 0
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*15)
    if n < 0:
        break
    else:
        while cont != 10:
            cont += 1
            resul = n * cont
            print(f'{n} x {cont} = {resul}')
        print('-'*15)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
