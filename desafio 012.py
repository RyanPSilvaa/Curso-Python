preco = float(input('Qual o preço do produto? R$ '))
novo = preco -(preco * 5 / 100)
print('O produto custava R${}, na promoção com 5% de desconto vai custar R${}'.format(preco, novo))
