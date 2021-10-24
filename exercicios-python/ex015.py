# Aluguel de carros
dias = int(input('Por quantos dias o carro foi alugado? '))
dist = float(input('Qual foi a quilometragem percorrida? '))
valordia = dias * 60
valorkm = dist * 0.15
valortotal = valordia + valorkm
print('De acordo com os dados fornecidos o valor a ser pago pelo aluguel do veículo é R${:.2f}'.format(valortotal))