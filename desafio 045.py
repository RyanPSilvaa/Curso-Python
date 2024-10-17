# Jokenpô
print('=-='*10)
print('JOKENPÔ')
print('=-='*10)
computador = ['Pedra', 'Papel', 'Tesoura']
humano = str(input('Pedra, Papel ou Tesoura?: '))

if humano == 'Pedra':
    print('HAHA, coloco Papel')
elif humano == 'Tesoura':
    print('HAHA coloquei, Papel!')
elif humano == 'Papel':
    print('HAHA, coloquei tesoura')
else:
    print('Por favor, digite um valor')