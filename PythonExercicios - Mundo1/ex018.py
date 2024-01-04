from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
a = radians(ang)
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sin(a)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos(a)))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan(a)))
