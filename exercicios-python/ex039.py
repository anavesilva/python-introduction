from datetime import date
ano = int(input('Ano de nascimento: '))
print('[ 1 ] Masculino  [ 2 ] Feminino')
sexo = int(input('Qual o seu sexo: '))
hoje = date.today().year
idade = hoje - ano
if idade < 18 and sexo == 1:
    print('Você tem hoje {} anos e deverá se alistar ao serviço militar em {} anos, no ano de {}.'.format(idade, 18 - idade, ano + 18))
elif idade == 18 and sexo == 1:
    print('Você tem hoje {} anos e portanto deverá de alistar ao serviço militar já neste ano de {}.'.format(idade, hoje))
elif idade > 18 and sexo == 1:
    print('Você tem {} anos e o seu tempo de alistamento expirou à {} anos, no ano de {}.'.format(idade, idade - 18, ano + 18))
else:
    print('Como você é do sexo feminino, não será obrigatório o alistamento no serviço militar.')