import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]               # Sempre use colchetes ao fazer uma lista
print('O aluno escolhido foi {}.'.format(random.choice(lista)))

# Lembrar de criar uma variável q contenha as opções a serem escolhidas pela função choice
