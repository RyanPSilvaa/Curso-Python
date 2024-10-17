n1 = float(input('Digite sua nota da prova 1:'))
n2 = float(input('Digite sua nota da prova 2:'))
media = (n1+n2) / 2
print('Sua média é {}'.format(media))
if media >= 8:
    print('Parabéns você passou!')
else:
    print('Você precisa fazer PF!')