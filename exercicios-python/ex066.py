cont = n = soma = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print('Foram digitados {} números e a soma entre eles é {}.'.format(cont, soma))