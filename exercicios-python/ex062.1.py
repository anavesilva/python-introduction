print('=' * 35)
print('OS 10 PRIMEIROS TERMOS DE UMA PA')
print('=' * 35)
termo1 = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão: '))
termo = termo1
c = 1
total = 0
mais = 10
print('Os 10 primeiros termos da PA são = ')
while mais != 0:
    total = total + mais
    while c <= total:
        termo += razao
        c +=1
        print('{}'.format(termo), end='-')
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('Prograssão finalizada com {} termos mostrados '.format(total))
