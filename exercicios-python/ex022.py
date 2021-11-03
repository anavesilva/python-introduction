# Analisador de textos 
nome = str(input('Digite o seu nome completo:')).strip()
print('Analizando o seu nome...')
print('O seu nome em letra maiúscula é {}'.format(nome.upper()))
print('O seu nome em letra minúscula é {}'.format(nome.lower()))
print('O seu nome apresenta {} letras'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
