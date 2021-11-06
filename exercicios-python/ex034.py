# Aumentos múltiplos
salario = float(input('Qual é o valor do salário do funcionário? '))
if salario > 1250:
    ajuste = salario * 1.1
else:
    ajuste = salario * 1.15
print('O funcionário passa a receber um salário de R${:.2f}.'.format(ajuste))