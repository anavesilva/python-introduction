#Exercício 41 – Classificando Atletas
from datetime import date
anoatleta = int(input('Ano de nascimento do atleta: '))
anoatual = date.today().year
idade = anoatual - anoatleta
print('A idade do atleta é {} anos.'.format(idade))
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JÚNIOR')
elif idade <= 25:
    print('Categoria SÊNIOR')
elif idade > 25: 
    print('Categoria MASTER')
