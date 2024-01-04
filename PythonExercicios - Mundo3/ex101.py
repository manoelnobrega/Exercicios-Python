from datetime import date


def voto(idade=0):
    if idade < 16:
        return "NÃO VOTA"
    elif 18 > idade >= 16 or idade > 70:
        return "VOTO FACULTATIVO"
    else:
        return "VOTO OBRIGATÓRIO"


ano = date.today().year - int(input('Em que ano você nasceu? '))
if voto(ano):
    print(f'Com {ano} anos', end=' ')
print(voto(ano))
