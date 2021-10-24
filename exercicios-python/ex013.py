#Reajuste salarial
salario = float(input('Digite o salário do funcionário: R$ '))
reajuste = salario * 1.15
print('O funcionário que ganhava R${:.2f}, após o reajuste passará a receber um salário no valor de R${:.2f}'.format(salario, reajuste))