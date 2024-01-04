tempCelsius = float(input('Informe a temperatura em ºC : '))
tempFahren = (tempCelsius * 9/5) + 32
tempKelvin = tempCelsius + 273.15
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF e a {:.2f}K'.format(tempCelsius, tempFahren, tempKelvin))
