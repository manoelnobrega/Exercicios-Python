def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def metade(n):
    n = n/2
    return n


def dobro(n):
    n = n*2
    return n


def aumento(n, t=100):
    n += n*(t/100)
    return n
