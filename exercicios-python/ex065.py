#n = cont = soma = 
soma = quant = media = maior = menor = 0
r = 'S'
while r in 'Ss':
    n = int(input('Digite um número inteiro: '))
    quant += 1
    soma += n
    media = soma/quant
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
print('Você digitou {} números e a média entre os números foi {:.2f}.'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
