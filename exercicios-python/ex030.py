# Par ou ímpar
numero = int(input('Digite um numero qualquer: '))
par = numero/2
resto = numero % 2
if resto == 0:
    print('O número {} é PAR.'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))