lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
        print('Adicionado ao final da lista...')
    elif c == 1:
        if n > lista[0]:
            lista.append(n)
            print('Adicionado ao final da lista...')
        else:
            lista.insert(0, n)
            print('Adicionado na posição 0 da lista...')
    elif c == 2:
        if n > lista[0] and n > lista[1]:
            lista.append(n)
            print('Adicionado ao final da lista...')
        elif lista[1] > n > lista[0]:
            lista.insert(1, n)
            print('Adicionado na posição 1 da lista...')
        else:
            lista.insert(0, n)
            print('Adicionado na posição 0 da lista...')
    elif c == 3:
        if n > lista[0] and n > lista[1] and n > lista[2]:
            lista.append(n)
            print('Adicionado ao final da lista...')
        elif lista[2] > n > lista[1]:
            lista.insert(2, n)
            print('Adicionado na posição 2 da lista...')
        elif lista[1] > n > lista[0]:
            lista.insert(1, n)
            print('Adicionado na posição 1 da lista...')
        else:
            lista.insert(0, n)
            print('Adicionado na posição 0 da lista...')
    elif c == 4:
        if n > lista[0] and n > lista[1] and n > lista[2] and n > lista[3]:
            lista.append(n)
            print('Adicionado ao final da lista...')
        elif lista[3] > n > lista[2]:
            lista.insert(3, n)
            print('Adicionado na posição 3 da lista...')
        elif lista[2] > n > lista[1]:
            lista.insert(2, n)
            print('Adicionado na posição 2 da lista...')
        elif lista[1] > n > lista[0]:
            lista.insert(1, n)
            print('Adicionado na posição 1 da lista...')
        else:
            lista.insert(0, n)
            print('Adicionado na posição 0 da lista...')
print(f'{"-="*30}\nOs valores digitados em ordem foram {lista}')

'''RESOLUÇÃO GUANABARA:
lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f'{"-="*30}\nOs valores digitados em ordem foram {lista}')
'''
'''RESOLUÇÃO ALTERNATIVA:
import bisect
numbers = []
for i in range(5):
    n = int(input('Type a number: '))
    bisect.insort(numbers, n)
    print(f'Number {n} included in position {numbers.index(n)}')
print(f'Numbers typed: numbers')
'''
