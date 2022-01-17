print('=' * 35)
print('OS 10 PRIMEIROS TERMOS DE UMA PA')
print('=' * 35)
termo1 = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão: '))
c = 0
maistermos = 0
ntottermos = 10
print('Os 10 primeiros termos da PA são = ')
while c < ntottermos:
    ultimo = termo1 + (c * razao)  
    c += 1
    print('{}'.format(ultimo), end='-')
    if c == ntottermos:
        print('Pausa')
        maistermos = int(input('Quantos termos a mais você quer saber? ')) 
        ntottermos += maistermos
print('Prograssão finalizada com {} termos mostrados.'.format(ntottermos))

