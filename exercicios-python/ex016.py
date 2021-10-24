# Quebrando um número
# math.trunc = separa a parte inteira | floor = arredonda para baixo | função int (não precisa importar)
import math
num = float(input('Digite um valor:'))
inteiro = math.trunc(num)
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, inteiro))
