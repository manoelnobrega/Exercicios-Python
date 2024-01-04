frase = str(input('Digite uma frase: ')).strip().upper().split()
frase_junta = ''.join(frase)
frase_inversa = frase_junta[::-1]
print('O inverso de {} é {}'.format(frase_junta, frase_inversa))
if frase_junta == frase_inversa:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

'''
com o uso do for:
frase_inversa = ''
for letra in range(len(frase_junta) - 1, -1, -1):
    frase_inversa += frase_junta[letra]
'''