from urllib import request as r
from urllib import error as e

try:
    r.urlopen('https://pudim.com.br/')
    print('\033[0;32mConsegui acessar o site pudim com sucesso!\033[m')
except e.URLError:
    print('\033[0;31mO site pudim não está acessível neste momento.\033[m')
