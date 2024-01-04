from datetime import date
ano = int(input('Ano de nascimento: '))
hoje = date.today().year
idade = hoje - ano
alistar = ano + 18
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, hoje))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    dif = hoje - alistar
    print('Você já deveria ter se alistado há {} anos\nSeu alistamento foi em {}.'.format(dif, alistar))
else:
    dif = alistar - hoje
    print('Ainda faltam {} anos para o alistamento\nSeu alistamento será em {}.'.format(dif, alistar))
