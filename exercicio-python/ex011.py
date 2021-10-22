# Pintando parede
largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))
area = (largura*altura)
print('A sua parede tem a dimensão de {}x{} que corresponde à uma área de {} m².\n---Para pintar esta parede serão necessários {} litros de tinta---'.format(largura, altura, area, area/2 ))