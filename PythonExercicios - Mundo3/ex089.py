nome = list()
nota1 = list()
nota2 = list()
boletim = [nota1, nota2]
while True:
    nome.append(str(input('Nome: ')).strip())
    nota1.append(float(input('Nota 1: ')))
    nota2.append(float(input('Nota 2: ')))
    opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opc not in 'SN':
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break
print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*24)
for i, n in enumerate(nome):
    media = (boletim[0][i] + boletim[1][i]) / 2
    print(f'{i:<4}{n:<10}{media:>8.1f}')
while True:
    print('-'*35)
    nota_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if nota_aluno in range(0, len(nome)):
        print(f'As notas de {nome[nota_aluno]} são {boletim[0][nota_aluno]} e {boletim[1][nota_aluno]}')
    else:
        if nota_aluno == 999:
            print('FINALIZANDO...')
            break
        else:
            print('Esse aluno não existe! Tente novamente:')
print('<<< VOLTE SEMPRE >>>')