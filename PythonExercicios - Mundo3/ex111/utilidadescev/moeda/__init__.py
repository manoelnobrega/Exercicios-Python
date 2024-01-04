def moeda(preco=0, sigla='R$'):
    """
    -> Formata um número tranformando-o em uma moeda
    :param preco: valor numérico a ser inserido
    :param sigla: moeda para a formatação (padrão em Real/BRL/R$)
    :return: retorna um texto formatado
    """
    return f'{sigla}{preco:.2f}'.replace('.', ',')


def metade(n, form=True):
    """
    -> Mostra a metade do valor informado
    :param n: valor numérico a ser inserido
    :param form: formata o valor usando a função 'moeda()'
    :return: retorna o valor formatado ou não
    """
    n = n/2
    if form:
        return moeda(n)
    else:
        return n


def dobro(n, form=True):
    """
    -> Mostra o dobro do valor informado
    :param n: valor numérico a ser inserido
    :param form: formata o valor usando a função 'moeda()'
    :return: retorna o valor formatado ou não
    """
    n = n*2
    if form:
        return moeda(n)
    else:
        return n


def aumento(n, t=100, form=True):
    """
    -> Mostra o valor somado a uma porcentagem
    :param n: valor numérico a ser inserido
    :param t: porcentagem a ser somado ao valor numérico
    :param form: formata o valor usando a função 'moeda()'
    :return: retorna o valor formatado ou não
    """
    n += n*(t/100)
    if form:
        return moeda(n)
    else:
        return n


def resumo(n, aum, red):
    """
    -> Simplifica todas as funções deste pacote e mostra na tela informações como o dobro, a metade, etc.
    :param n: valor numérico a ser inserido
    :param aum: porcentagem a ser somado ao valor numérico
    :param red: porcentagem a ser substraída ao valor numérico
    :return: retorna uma tabela com o dobro, a metade, uma porcentagem de aumento e redução
    """
    d = n * 2
    met = n / 2
    p1 = n + n * (aum / 100)
    p2 = n - n * (red / 100)
    lin = '-' * 30
    linha1 = f'Preço analisado: {"R$":>9}{n:.2f}'.replace('.', ',')
    linha2 = f'Dobro do preço: {"R$":>10}{d:.2f}'.replace('.', ',')
    linha3 = f'Metade do preço: {"R$":>9}{met:.2f}'.replace('.', ',')
    linha4 = f'{aum}% de aumento: {"R$":>10}{p1:.2f}'.replace('.', ',')
    linha5 = f'{red}% de redução: {"R$":>10}{p2:.2f}'.replace('.', ',')
    cabecalho = f'{"RESUMO DO VALOR":^30}'
    return print(f'{lin}\n{cabecalho}\n{lin}\n{linha1}\n{linha2}\n{linha3}\n{linha4}\n{linha5}\n{lin}')
