salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    salarioNovo = salario * 1.15
else:
    salarioNovo = salario * 1.10
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, salarioNovo))
