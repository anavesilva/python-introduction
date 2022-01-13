import random
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
#Definir os números a serem escolhidos pelo computador 
lista = range(1, 11)
computador = random.choice(lista)

acertou = False
#Contagem de tentativas 
tentativa = 0
while acertou == False:
    jogador = int(input('Em que número eu pensei? '))
    tentativa += 1
    if computador == jogador:
        acertou = True
        print('Parabéns! você conseguiu me vencer com {} tentativas!'.format(tentativa))
    else:
        print('Tente novamente!')