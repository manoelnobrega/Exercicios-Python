from datetime import date
cadastro = dict()
cadastro["nome"] = str(input('Nome: ')).strip()
cadastro["idade"] = int(input('Ano de Nascimento: '))
cadastro["ctps"] = int(input('Carteira de Trabalho (0 não tem): '))
hoje = date.today().year
cadastro["idade"] = hoje - cadastro["idade"]
if cadastro["ctps"] != 0:
    cadastro["contratação"] = int(input('Ano de Contratação: '))
    cadastro["salário"] = float(input('Salário: R$'))
    cadastro["aposentadoria"] = ((cadastro["contratação"] + 35) - hoje) + cadastro["idade"]
print('-='*30)
for k, v in cadastro.items():
    print(f'  - {k} tem o valor {v}')
