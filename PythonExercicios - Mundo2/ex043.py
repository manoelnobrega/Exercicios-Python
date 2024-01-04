peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O seu Índice de Massa Corpórea (IMC) é de {:.1f} kg/m²'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25:
    print('PARABÉNS você está no PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE.')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
