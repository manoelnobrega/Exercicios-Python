from math import pow, sqrt
catO = float(input('Comprimento do cateto oposto: '))
catA = float(input('Comprimento do cateto adjacente: '))
h = pow(catO, 2) + pow(catA, 2)
print('A hipotenusa vai medir {:.2f}'.format(sqrt(h)))

# math.hypot() pode ser usada para o calculo da hipotenusa
