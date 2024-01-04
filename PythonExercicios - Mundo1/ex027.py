nome = str(input('Digite seu nome completo: ')).strip().split()
nomeContado = len(nome) - 1
print('Muito prazer em te conhecer!\nSeu primeiro nome é {}\nSeu último nome é {}'.format(nome[0], nome[nomeContado]))
