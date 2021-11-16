nome = str(input('Qual é o seu nome? '))
if nome == 'Ana':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Enzo' or nome == 'Valentina':
    print('Seu nome é bem popular na Brasil!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia {}!'.format(nome))