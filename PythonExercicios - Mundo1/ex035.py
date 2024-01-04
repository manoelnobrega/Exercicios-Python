import emoji
import time
print('-=-'*12)
print(emoji.emojize('Analisador de Triângulos :red_triangle_pointed_up: :triangular_ruler: :straight_ruler:'))
print('-=-'*12)
time.sleep(1.70)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < c + a and c < b + a:
    print(emoji.emojize('Os segmentos acima PODEM formar um triângulo! :beaming_face_with_smiling_eyes:'))
else:
    print(emoji.emojize('Os segmentos acima NÃO PODEM formar um triângulo! :crying_face:'))
