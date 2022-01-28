import random
print('-=' * 15)
print('  VAMOS JOGAR PAR OU ÍMPAR?!')
print('-=' * 15)
lista = range(1, 11)
computador = random.choice(lista)
result = ''
x = ''
cont = 0
while x == result:
    v = int(input('Digite um valor: '))
    x = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    soma = v + computador
    if soma % 2 == 0:
        result = 'P'
    else:
        result = 'I'
    if result == 'I':
        resultname = 'ÌMPAR'
    else:
        resultname = 'PAR'
    print('Você jogou {} e o computador {}. O total de {} que é {}'.format(v, computador, soma, resultname))
    print('-=' * 15)
    if x == result:
        print('Você ganhou!')
        print('Vamos jogar novamente ...')
        cont += 1
    else:
        break
        print('Você perdeu!')
    print('-=' * 15)
print('GAME OVER! Você ganhou {} vezes.'.format(cont))