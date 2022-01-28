print('=' * 20)
print('       LOJA')
print('=' * 20)

tot_compra = cont1000 = 0
barato = 0
cont = 0
prodbarato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))
    continuar = ''
    tot_compra += preco
    cont += 1
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
    if preco >= 1000:
        cont1000 += 1
    if cont == 1:
        barato = preco
        prodbarato = produto
    else:
        if preco < barato:
            barato = preco
            prodbarato = produto

    if continuar == 'N':
        break 
print('{:-^40}'.format(' FIM DO PROGRAMA '))    
print('Valor total da compra: R$ {:.2f}.'.format(tot_compra))
print('Entre os produtos contidos na lista {} custaram mais de R$ 1000,00'.format(cont1000))
print('O produto mais barato foi o {}.'.format(prodbarato))
    