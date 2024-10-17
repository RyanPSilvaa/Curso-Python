# IMC
nome = str(input('Digite seu nome:'))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
resultado  = peso / (altura*altura)

if resultado < 18.5:
    print('Olá {} Abaixo do peso'.format(nome))
elif 18.5 <= resultado < 25:
    print('Olá {} você está no peso ideal!'.format(nome))
elif 25 <= resultado < 30:
    print('Olá {} você está acima do peso'.format(nome))
elif 30 <= resultado < 40:
    print('Olá {} você está obeso!'.format(nome))
elif resultado >= 40:
    print('Olá {} você está com obesidade mórbida!'.format(nome))