print("Aumento salarial de 15%")
s = float(input("Digite o salário de um funcionário: "))
a = s + (s * 15 / 100)
print("O antigo salário do funcionário era de R${} e com o aumento será de R${:.2f}".format(s,a))
