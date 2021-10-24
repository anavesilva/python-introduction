#Conversor de moeda
moeda = float(input('Quanto dinheiro você tem na disponível? R$'))
print('Com o valor de R${:.2f} você pode comprar US${:.2f}'.format(moeda, moeda/5.67))
print('Com o valor de R${:.2f} você pode comprar EUR{:.2f}'.format(moeda, moeda/6.60))
print('Com o valor de R${:.2f} você pode comprar £{:.2f}'.format(moeda, moeda/7.80))
