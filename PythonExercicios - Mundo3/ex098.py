def contador(inicio, fim, passo):
    from time import sleep
    print('-=' * 30)
    if inicio > fim:
        print(f'Contagem de {inicio} até {fim} de {-passo} em {-passo}')
        fim -= 1
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        fim += 1
    for num in range(inicio, fim, passo):
        sleep(0.3)
        print(num, end=' ')                    # Caso ocorra buffering de tela use flush='True' após o print
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

'''
# Resolução Guanabara:
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
        
        
        
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
'''
