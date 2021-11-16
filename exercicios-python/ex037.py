#Conversor de base numérica
numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O número {} convertido para BINÁRIO é igual a {}.'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('O número {} convertido para OCTAL é igual a {}.'.format(numero, oct(numero)[2:])) 
elif opção ==3:
    print('O número {} convertido para HEXADECIMAL é igual a {}.'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Verifique se o número digitado se encontra nas opções de conversão acima.')
