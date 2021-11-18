#Exercício 44 – Gerenciador de Pagamentos
print('{:=^40}'.format(' LOJAS GUANABARA '))
produto = float(input('Valor do produto: R$ '))
print('''Selecione a forma de pagamento: 
[ 1 ] à vista dinheiro/cheque: 10% de desconto
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão: preço normal 
[ 4 ] 3x ou mais no cartão: 20% de juros''')
forma = int(input('Forma de pagamento: '))
f1 = produto * 0.9
f2 = produto * 0.95
f3 = produto
f4 = produto * 1.2
if forma == 1:
    print('O valor do produto com o desconto de 10% será R${:.2f}'.format(f1))
elif forma == 2:
    print('O valor do produto com o desconto de 5% será R${:.2f}'.format(f2))
elif forma == 3:
    parcela = int(input('Quantas parcelas:'))
    print('O valor do produto será R${:.2f}.'.format(f3))
    print('A compra poderá ser dividido em duas parcelas de R${}'.format(f3 / 2))
elif forma == 4:
    parcela = int(input('Quantas parcelas:'))
    print('O valor do produto será R${:.2f}'.format(f4))
    print('A compra poderá ser dividido em {} parcelas de R${:.2f}'.format(parcela, f4 / parcela))
else:
    print('Opção inválida.')