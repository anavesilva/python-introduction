n = 0
tab = 0
while True:
    n = int(input('Você deseja mostrar a tabuada do número: '))
    print('-' * 30)
    if n < 0:
        break
    for c in range (1, 10):
        c +=1
        tab = n * c
        print('{} X {} = {}'.format(n, c, tab))
    print('-' * 30)
print('Programa encerrado!')