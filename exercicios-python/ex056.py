somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomehomemmaisvelho = ''
mulherescommenosde20anos = 0
for c in range(1, 5): 
    print('-----{}º PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomehomemmaisvelho = nome 
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehome = idade
        nomehomemmaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulherescommenosde20anos += 1
    
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomehomemmaisvelho))
print('No grupo existem {} mulheres com menos de 20 anos.'.format(mulherescommenosde20anos))