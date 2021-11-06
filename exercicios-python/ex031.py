# Custo da viagem
distancia = float(input('Qual a distância da sua viagem? '))
valor1 = distancia * 0.5
valor2 = distancia * 0.45
print('Você está prestes a começar uma viagem de {}Km/h.'.format(distancia))
if distancia <= 200:
    print('O preço de sua passagem será de R${:.2f}.'.format(valor1))
else:
    print('O preço de sua passagem será de R${:.2f}.'.format(valor2))
