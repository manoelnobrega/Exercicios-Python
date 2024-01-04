import emoji
import time
print('-=-'*12)
print(emoji.emojize('Analisador de Triângulos :red_triangle_pointed_up: :triangular_ruler: :straight_ruler:'))
print('-=-'*12)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < c + a and c < b + a:
    if a == b == c:
        print(emoji.emojize('Os segmentos acima PODEM formar um triângulo EQUILÁTERO :beaming_face_with_smiling_eyes:'))
    elif a == b != c or b == c != a or c == a != b:
        print(emoji.emojize('Os segmentos acima PODEM formar um triângulo ISÓSCELES :beaming_face_with_smiling_eyes:'))
    elif a != b != c != a:
        print(emoji.emojize('Os segmentos acima PODEM formar um triângulo ESCALENO :beaming_face_with_smiling_eyes:'))
else:
    print(emoji.emojize('Os segmentos acima NÃO PODEM formar um triângulo! :crying_face:'))
