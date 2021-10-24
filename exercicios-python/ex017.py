# Catetos e hipotenusa
# h = math.sqrt((co**2) + (ca**2))
import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
h = math.hypot(co, ca)
print('O valor da hipotenusa será {:.2f}'.format(h))