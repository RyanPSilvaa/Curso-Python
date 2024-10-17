distancia = float(input('Qual é a distância da sua viagem?'))
print('Você vai percorre {}KM de distância'.format(distancia))

if distancia <= 200:
    preco = distancia * 0.50
    print('E o preço da passagem será de R${}'.format(preco))
else:
    preco = distancia * 0.45
    print('E o preço da passagem será de R${}'.format(preco))