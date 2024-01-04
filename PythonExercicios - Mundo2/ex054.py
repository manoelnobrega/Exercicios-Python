from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = ano_atual - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas maiores de idade\nE também tivemos {} pessoas menores de idade'.format(maior, menor))
