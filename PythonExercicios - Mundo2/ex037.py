num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, format(num, 'b')))      # bin(num)[2:]
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, format(num, 'o')))        # oct(num)[2:]
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, format(num, 'X')))  # hex(num)[2:]
