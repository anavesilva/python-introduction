#Verificando as primeiras letras de um texto
nome = str(input('Qual é o seu nome completo? ')).strip()
#temsilva = 'SILVA' in nome
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))