print('-' * 32)
print(' SISTEMA DE CADASTRO DE PESSOAS')
print('-' * 32)
conthmais18 = 0
conthomes = 0
contmmenos20 = 0
continuar = ''
while True: 
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).upper().strip()
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if idade > 18:
        conthmais18 += 1
    if sexo == 'M':
       conthomes += 1
    if sexo == 'F':
        if idade < 20:
            contmmenos20 +=1
    if continuar == 'N':
        break
print('=' * 6, 'FIM DO PROGRAMA', '=' * 6)
print('Total de pessoas com mais de 18 anos: {} '.format(conthmais18))
print('Ao todo temos {} homens cadastrados.'.format(conthomes))
print('Total de mulheres com menos de 20 anos: {}'.format(contmmenos20))