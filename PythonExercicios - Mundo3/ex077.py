palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
print('-'*40)
print(f'{"RECONHECENDO VOGAIS":^40}')
print('-'*40)
for p in palavras:
    print(f'Na palavra {p.upper()} temos:', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print('\n', end='')
print('-'*40)
