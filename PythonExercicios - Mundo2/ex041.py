from datetime import date
ano = int(input('Ano de Nascimento: '))
hoje = date.today().year
idade = hoje - ano
print('O atleta tem {} anos.'.format(idade))
print('Classificação: ', end='')
if idade <= 9:
    classif = 'MIRIM'
elif 9 < idade <= 14:
    classif = 'INFANTIL'
elif 14 < idade <= 19:
    classif = 'JUNIOR'
elif 19 < idade <= 25:
    classif = 'SÊNIOR'
else:
    classif = 'MASTER'
print(classif)