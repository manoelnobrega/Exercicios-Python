num = int(input('Informe um número: '))
print('Analisando o número {}'.format(num))
numU = num % 10
numD = num // 10
numC = num // 100
numM = num // 1000
print('Unidade: {}'.format(numU))
print('Dezena: {}'.format(numD % 10))
print('Centena: {}'.format(numC % 10))
print('Milhar: {}'.format(numM % 10))
