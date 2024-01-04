numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', \
    'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
valor = int(input('Digite um número entre 0 e 20: '))
while valor > 20 or valor < 0:
    print('Tente novamente.', end=' ')
    valor = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros[valor]}.')
