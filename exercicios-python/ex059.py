from time import sleep
a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))

m = 0
print('=-' * 15)
while m != 5:
    print('''
    Menu
    [1] Somar 
    [2] Multiplicar 
    [3] Maior 
    [4] Novos números 
    [5] Sair do programa''')

    m = int(input('>>>>>Selecione o próximo passo: '))
    print('=-' *15) 
    if m == 1: 
        s = a + b
        print('A soma entre {} e {} é {}.'.format(a, b, s))
    elif m == 2:
        mu = a * b
        print('A multiplicação entre {} e {} é {}.'.format(a, b, mu))
    elif m == 3:
        if a > b:
            print('O maior número é o {}.'.format(a))
        elif a < b:
            print('O maior número é o {}.'.format(b))
        else:
            print('Os números selecionados são iguais!')
    elif m == 4:
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
    elif m == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Digite apenas as opções do menu!')
    print('=-' *15) 
    sleep(2)
print('Programa finalizado!')
print('=-' *15) 

