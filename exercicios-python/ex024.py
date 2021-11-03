# Verificando as primeiras letras de um texto
# cidade = str(input('Em que cidade você nasceu?')).strip()
# print(cidade)
# unificado = cidade.upper()
# print(unificado)
# print('SANTO ' in unificado[:6])
cidade = str(input('Em que cidade você nasceu? ')).strip().upper().split(' ')
print('SANTO' == cidade[0])

