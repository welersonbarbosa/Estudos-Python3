# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input('Informe um valor para n1: '))
n2 = int(input('Informe um valor para n2: '))
n3 = float(input('Informe um valor para n3: '))

dobron1 = n1*2
triplon1 = n1*3
cubon3 = n3**3


print('\nO produto do dobro do primeiro com metade do segundo = {}'.format(dobron1+n2/2))
print('A soma do triplo do primeiro com o terceiro. = {}'.format(triplon1 + n3))
print('O terceiro elevado ao cubo. = {}'.format(cubon3))
