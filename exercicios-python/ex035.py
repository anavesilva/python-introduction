# Analisando Triângulo v1.0
#a soma de dois lados é sempre menor que o terceiro lado.
print('-=-' * 10)
print('Analisador de triangulos')
print('-=-' * 10)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
soma12 = r1 + r2
soma13 = r1 + r3
soma23 = r2 +r3
if soma12 > r3 and soma13 > r2 and soma23 > r1:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos fornecidos acima NÃO podem formar um triângulo!')
