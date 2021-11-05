#Jogo da adivinhação
import random
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
lista = [1, 2, 3, 4, 5]
computador = random.choice(lista)
print('PROCESSANDO...')
sleep(3)
if computador == jogador:
    print('Parabéns! você conseguiu me vencer!')
else:
    print('Guanhei! Eu pensei no número {} e não no {}.'.format(computador, jogador))
