# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

print('Iremos calcular o total de seu salário')
print('Preencha corretamente os dados abaixo: ')

print ('-'*40) #Apenas para organizar o código


n1 = float(input("\nQuanto você recebe por horas: R$ "))
n2 = float(input("Quantas horas você trabalhou esse mês: "))

total = n1*n2 #Calculando salário total

print ('-'*40) #Apenas para organizar o código

print('O seu salário total é R$ {} '.format(total))
