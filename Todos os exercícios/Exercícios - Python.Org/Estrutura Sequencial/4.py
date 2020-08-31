# 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print( 'Iremos calcular a sua média final.\n')

n1 = int(input('Informe a média do 1° bimestre: '))
n2 = int(input('Informe a média do 2° bimestre: '))
n3 = int(input('Informe a média do 3° bimestre: '))
n4 = int(input('Informe a média do 4° bimestre: '))

notaf = (n1 + n2 + n3 + n4)/4

print('\nA sua média final é {}'.format(notaf))

