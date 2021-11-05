# Radar eletronico
velocidade = int(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Tenha um bom dia e dirija com segurança!')
else: 
    print('MULTADO! Você excedeu o limite de velocidade de 80Km/h em {}Km/h.'.format(velocidade-80))
    print('Você deverá pagar uma multa de {:.2f}.'.format(multa))
