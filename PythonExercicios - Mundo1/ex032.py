import time
ano = str(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == '0':
    anoHoje = time.strftime('%Y')                     # -------> pega o ano atual
    string1 = '31 Dec {}'.format(anoHoje)
    analise1 = time.strptime(string1, '%d %b %Y')     # -------> tem q entrar com uma string
    diasHoje = analise1[7]                            # -------> analise o 7º objeto do strptime
    if diasHoje <= 365:
        print('O ano {} NÃO é BISSEXTO'.format(anoHoje))
    else:
        print('O ano {} é BISSEXTO'.format(anoHoje))
else:
    string2 = '31 Dec {}'.format(ano)
    analise2 = time.strptime(string2, '%d %b %Y')
    dias = analise2[7]
    if dias <= 365:
        print('O ano {} NÃO é BISSEXTO'.format(ano))
    else:
        print('O ano {} é BISSEXTO'.format(ano))


'''

RESOLUÇÃO DO GUANABARA:

from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else
    print('O ano {} NÃO é BISSEXTO'.format(ano))
    
'''
