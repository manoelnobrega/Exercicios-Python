from time import sleep
from random import choice
print('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
play = int(input('Qual é a sua jogada? '))
options = ['Pedra', 'Papel', 'Tesoura']
option_computer = choice(options)
if play > 2 or play < 0:
    print('\033[1;31mERRO!!!\033[m\nDigite um valor válido.')     # mensagem de erro caso número não corresponder
else:
    sleep(0.5)
    print('JO')
    sleep(0.75)
    print('KEN')
    sleep(0.75)
    print('PO!!!')
    sleep(0.75)
    print('-='*11)
    print('Computador jogou {}'.format(option_computer))
    print('Jogador jogou ', end='')
    # atribuindo as strings à variável 'play'
    if play == 0:
        play = 'Pedra'
        print(play)
    elif play == 1:
        play = 'Papel'
        print(play)
    elif play == 2:
        play = 'Tesoura'
        print(play)
    print('-='*11)
    # aqui vem a 'batalha'
    if option_computer == play:
        print('EMPATE')
    else:
        if option_computer == 'Pedra' and play == 'Tesoura' or option_computer == 'Papel' and play == 'Pedra' or \
                option_computer == 'Tesoura' and play == 'Papel':
            print('COMPUTADOR VENCE')
        else:
            print('JOGADOR VENCE')
