from webbrowser import Elinks


xn = int(input('Digite um número de termos da Sequência de Fibonacci você deseja ver: '))
x1 = 0
x2 = 1
c = 0
acc = 0
while c < xn:
    if c == 0:
        print(x1, end='-')
    elif c == 1:
        print(x2, end= '-')
    else:
        acc = x1 + x2
        print(acc, end='-')
        x1 = x2
        x2 = acc
    c += 1
print('FIM')
