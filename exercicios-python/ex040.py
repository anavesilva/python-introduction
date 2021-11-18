#Exercício 40 – Aquele clássico da Média
prova1 = float(input('Nota da primeira prova: '))
prova2 = float(input('Nota da segunda prova: '))
prova3 = float(input('Nota da terceita prova: '))
media = (prova1 + prova2 + prova3)/3
if media < 5:
    print('A sua média foi {:.1f} pontos. O aluno está reprovado.'.format(media))
elif media >= 5 and media < 7:
    print('A sua média foi {:.1f} pontos. O aluno está de recuperação.'.format(media))
else:
    print('A sua média foi de {:.1f} pontos. O aluno está APROVADO!'.format(media))
