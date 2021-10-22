# Calculando descontos 
valor = float(input('Digite o valor do  produto: R$ '))
desc = valor * 0.95
print('O produto que custa R${:.2f}, na promoção com desconto de 5%, passá a custar R${:.2f}'.format(valor, desc))
