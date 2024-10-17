vel = int(input('Digite a velocidade do carro:'))

if vel > 80:
    print('Você ultrapassou o limite de 80KM/H você estava a {}KM/H'.format(vel))
    multa = vel * 7
    print('Você vai pagar uma multa de {:.2f}'.format(multa))
else:
    print('Bom dia... continue dirigindo com segurança')
