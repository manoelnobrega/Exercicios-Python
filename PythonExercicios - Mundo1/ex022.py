nome = str(input('Qual é o seu nome?')).strip()
print('Este é o seu nome em maiúsculas: {}'.format((nome.upper())))
print('Este é o seu nome em minúsculas: {}'.format(nome.lower()))
nome2 = nome.split()
nomeContado = ''.join(nome2)
print('Esta é a quantidade de letras do seu nome: {}'.format(len(nomeContado)))
print('Esta é a quantidade de letras no primeiro nome: {}'.format(len(nome2[0])))
