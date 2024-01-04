def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    med = 0
    for i in range(len(n)):
        med += n[i]
    med = med/len(n)
    dicio = {'total': len(n),
             'maior': max(n),
             'menor': min(n),
             'média': med,                       # mean(n) tbm funciona!
             'situação': ''}
    if sit:
        if med < 5:
            dicio['situação'] = 'RUIM'
        elif 6.5 >= med >= 5:
            dicio['situação'] = 'RAZOÁVEL'
        elif 8 > med > 6.5:
            dicio['situação'] = 'BOA'
        elif med >= 8:
            dicio['situação'] = 'EXCELENTE'
    else:
        del dicio['situação']
    return dicio


resp = notas(5, 10, 3, sit=True)
print(resp)
