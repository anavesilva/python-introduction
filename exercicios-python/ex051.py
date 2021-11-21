#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('=' * 35)
print('OS 10 PRIMEIROS TERMOS DE UMA PA')
print('=' * 35)
termo1 = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão: '))
ultimo = termo1 + (10) * razao
for c in range(termo1, ultimo, razao):
    ultimo = ultimo + razao
    print('{}'.format(c), end= '-')
print('FIM')
