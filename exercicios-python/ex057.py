s = str(input('Qual o seu sexo? [F/M] ')).strip().upper()
while s not in 'FM':
    s = str(input('Valor inválido! Digite novamente!')).strip().upper()
print('OK! Entendemos que o seu sexo é {}.'.format(s))