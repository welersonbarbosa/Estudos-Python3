
# 10 Conversor de moedas

print("-"*15)
print("Conversor de Moedas")
c = float(input("Quanto de dinheiro você possui na carteira? : R$ "))
d = c / 5.51
e = c / 6.50
p = c * 13.37
l = c / 7.24
print("Com R$ {} você pode comprar: \n USD {:.2f} \n EUR {:.2f} \n ARS {:.2f} \n £ {:.2f}".format(c,d,e,p,l))
print("-"*15)
print("Desenvolvido por Welerson Barbosa.")
