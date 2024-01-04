from random import randint
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
num_comp = randint(0, 10)
# num = int(input('Qual é o seu palpite? '))
tent = 0
acertou = False
while not acertou:
    num = int(input('Qual é o seu palpite? '))
    tent += 1
    if num == num_comp:
        acertou = True
    else:
        if num > num_comp:
            print('Menos... Tente mais uma vez.')
        elif num < num_comp:
            print('Mais... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(tent))

'''
MINHA RESOLUÇÃO:
while num != num_comp:
    if num > num_comp:
        print('Menos... Tente mais uma vez.')
    elif num < num_comp:
        print('Mais... Tente mais uma vez.')
    num = int(input('Qual é o seu palpite? '))
    tent += 1
if num == num_comp:
    print('Acertou com {} tentativas. Parabéns!'.format(tent))
'''
