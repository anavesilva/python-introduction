n = 0
cont = 0
soma = 0
n = int(input('Digite um número inteiro (999 para parar): '))
while n != 999:
    cont += 1
    soma = soma + n
    n = int(input('Digite um número inteiro (999 para parar): '))
print('Foram digitados {} números, e a soma deles é {}.'.format(cont, soma))