lista = []
n = int(input('Digite um número: '))
opc = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
cont = 1
soma = n
lista += [n]
while opc == 'S':
    n = int(input('Digite um número: '))
    opc = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont += 1
    soma += n
    lista += [n]
print('Você digitou {} números e a média foi {}'.format(cont, soma / cont))
print('O maior valor foi {} e o menor foi {}'.format(max(lista), min(lista)))
# Utilizando 'max' e 'min' fica bem mais fácil
