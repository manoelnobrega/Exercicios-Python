def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = n
    for i in range(n-1, 0, -1):
        f *= i
    if show:
        print(n, end=' ')
        for i in range(n-1, 0, -1):
            print(f'x {i}', end=' ')
        print('=', end=' ')
        return f
    if not show:
        return f


print(fatorial(5, True))
