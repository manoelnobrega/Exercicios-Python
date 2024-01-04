maioridade = homens = mulheres_jovens = 0
while True:
    print('-'*26)
    print('CADASTRE UMA PESSOA'.center(26, ' '))
    print('-'*26)
    # Verificando a maioridade:
    idade = int(input('Idade: '))
    if idade > 18:
        maioridade += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    # Verificando se a opção 'sexo' está correta:
    if sexo in 'Mm':
        homens += 1
    elif sexo in 'Ff':
        if idade < 20:
            mulheres_jovens += 1
    else:
        while sexo not in 'MmFf':
            sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-'*26)
    # Verificando se quer continuar:
    opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opc in 'Ss':
        print('', end='')
    elif opc in 'NnÑñ':
        break
    else:
        while opc not in 'Ss':
            opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if opc in 'NnÑñ':
                break
        if opc in 'NnÑñ':
            break
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homens} homens cadastrados\nE temos {mulheres_jovens} mulheres com menos de 20 anos')
