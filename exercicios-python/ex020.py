# Sorteando uma ordem na lista
import random
a1 = str(input('Primeirx alunx:'))
a2 = str(input('Segundx alunx:'))
a3 = str(input('Terceirx alunx:'))
a4 = str(input('Quartx alunx:'))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será {}.'.format(lista))
