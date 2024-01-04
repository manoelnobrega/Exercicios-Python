pessoas = list()
pessoa = dict()
soma_idades = 0
while True:
    pessoa["nome"] = str(input('Nome: ')).strip()
    pessoa["sexo"] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while pessoa["sexo"] not in 'MF':
        print('ERRO! Por favor digite M ou F')
        pessoa["sexo"] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoa["idade"] = int(input('Idade: '))
    soma_idades += pessoa["idade"]
    pessoas.append(pessoa.copy())
    pessoa.clear()
    opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opc not in 'SN':
        print('ERRO! Por favor digite S ou N')
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break
media_idades = soma_idades/len(pessoas)
print('-='*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media_idades:.2f} anos.')
print(f'C) As mulheres cadastradas foram', end=' ')
for c in range(0, len(pessoas)):
    if pessoas[c]["sexo"] == 'F':
        print(pessoas[c]["nome"], end=' ')
print('\nD) Lista das pessoas que estão acima da média:')
for c in range(0, len(pessoas)):
    if pessoas[c]["idade"] > media_idades:
        for k, v in pessoas[c].items():
            print(f'    {k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
