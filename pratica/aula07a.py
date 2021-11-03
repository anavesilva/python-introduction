# Operadores aritméticos: mais(+), subtração(-), multiplicação(*), divisão(/), 
# potência(**)|pow(,),
# divisão inteira(//), resto da divisão(%), igual(==) 
# Ordem de precedência: 1- () |2- ** |3- *, /, //, % |4- +, -
n1=int(input('Digite um valor:'))
n2=int(input('Digite outro valor:'))
s= n1+n2
m= n1*n2
d= n1/n2
di= n1//n2
e= n1**n2
print('A soma é {}, a divisão é {}, e a multiplicação é {:.3f}.'.format(s,m,d), end='---')
print('A divisão inteira é {} e a potência é {}'.format(di,e))
