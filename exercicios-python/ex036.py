# Aprovar emprestimo bancário 
valorcasa = float(input('Qual o valor da casa? R$ ' ))
valorsalario = float(input('Qual o valor do seu salário? R$ '))
tempo = int(input('Em quantos anos você pretende pagar?  '))
valordaparcela = valorcasa / (tempo * 12)
print('Para comprar uma casa no valor de R${:.2f} em {} anos, a parcela será de R${:.2f}.'.format(valorcasa, tempo, valordaparcela))
minimo = 0.3 * valorsalario
if valordaparcela < minimo:
    print('Emprestimo aprovado!')
else:
    print('Empéstimo não aprovado.')
