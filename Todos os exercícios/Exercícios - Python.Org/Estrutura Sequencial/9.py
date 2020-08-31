# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).



F = int(input('Informe a temperatura em graus Fahrenheit: '))
C = 5*((F-32)/9)

print('Você informou que a temperatura é {} °F'.format(F))
print('{} °F equivale a {}°C'.format(F,C))
