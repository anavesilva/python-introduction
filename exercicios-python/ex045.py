#Exercício 45 – GAME: Pedra Papel e Tesoura
from random import randint
from time import sleep
print('=' * 23)
print('PEDRA PAPEL TESOURA...')
print('=' * 23)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogada = int(input('Qual é a sua jogada: '))
lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=-' * 15)
print('O computador jogou {}.'.format(lista[computador]))
print('O jogador jogou {}.'.format(lista[jogada]))
print('=-' * 15)
if computador == 0:
    if jogada == 0:
        print('EMPATE')
    elif jogada == 2:
        print('COMPUTADOR VENCEU')
    elif jogada == 1:
        print('JOGADOR VENCEU')
elif computador == 1:
    if jogada == 1:
        print('EMPATE')
    elif jogada == 2:
        print('COMPUTADOR VENCEU')
    elif jogada == 0:
        print('JOGADOR VENCEU')
elif computador == 2:
    if jogada == 2:
        print('EMPATE')
    elif jogada == 1:
        print('COMPUTADOR VENCEU')
    elif jogada == 0:
        print('JOGADOR VENCEU')

