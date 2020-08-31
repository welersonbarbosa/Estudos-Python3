print(" ### Sistema de desconto ### ")
preço = float(input("Digite o preço do produto que deseja comprar: "))
print("Calculando desconto de 5% ")
v = preço * 5
d = v / 100
print(" O valor do seu desconto será de R$ {}".format(d))
