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
