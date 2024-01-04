aluno = dict()
aluno['nome'] = (str(input('Nome: '))).strip().capitalize()
aluno['média'] = (float(input(f'Média de {aluno["nome"]}: ')))
if aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
elif 7 > aluno['média'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'
print('-='*30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
