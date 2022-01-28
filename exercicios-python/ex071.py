print('=' * 20)
print('{:^20}'.format('CAIXA ELETRÔNICO'))
print('=' * 20)
print('O caixa apresenta cédulas de R$50, R$20, R$10 e R$1.')
ced = 50
totced = 0
valor = int(input('Qual valor você deseja sacar? R$ '))
total = valor
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print('Total de {} cédulas de R$ {}.'.format(totced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('OBRIGADO! VOLTE SEMPRE!')





