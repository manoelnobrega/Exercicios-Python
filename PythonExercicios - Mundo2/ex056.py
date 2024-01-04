media_idade = 0
meninas = 0
velho = 0
nome_velho = ''
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    # Verificando a média de idade:
    media_idade += idade
    # Verificando o homem mais velho:
    if c == 1:
        if sexo == 'M':
            velho = idade
            nome_velho = nome
    else:
        if idade > velho:
            velho = idade
            nome_velho = nome
    # Verificando mulheres com menos de 20 anos:
    if sexo == 'F' and idade < 20:
        meninas += 1
    # Mensagem de erro caso sexo não seja 'M' ou 'F':
    if sexo != 'M' and sexo != 'F':
        print('\033[1;31mERRO!!!\033[m sexo inválido, tente novamente.')
        break
print('A média de idade do grupo é de {} anos'.format(media_idade / 4))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(meninas))
