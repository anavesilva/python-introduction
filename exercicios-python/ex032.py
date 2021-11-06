#Ano bissexto -   com exceção dos múltiplos de 400, deverão ser anos bissextos.
from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
multiplo4 = ano % 4
multiplo400 = ano % 400
multiplo100 = ano % 100

if multiplo4 == 0 and multiplo100 != 0 or multiplo400 == 0: 
        print('O ano {} é bissexto!'.format(ano))   
else:
        print('O ano {} não é bissexto!'.format(ano))  
