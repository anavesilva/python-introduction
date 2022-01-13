print('=' * 35)
print('OS 10 PRIMEIROS TERMOS DE UMA PA')
print('=' * 35)
termo1 = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão: '))
c = 0
print('Os 10 primeiros termos da PA são = ')
while c < 10:
    ultimo = termo1 + (c * razao)  
    c +=1
    print('{}'.format(ultimo), end='-')
print('Pausa')
maistermos = int(input('Quantos termos a mais você quer saber? '))











while c < (10 + maistermos):
    ultimo = termo1 + (c * razao)
    c += 1
    if maistermos == 0:
        print('Acabou')
    print('{}'.format(ultimo), end='-')
print('Pausa')
maistermos = int(input('Quantos termos a mais você quer saber? '))
