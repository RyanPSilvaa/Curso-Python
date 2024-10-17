idade  = int(input('Digite a sua idade: '))

if idade <= 9:
    print('Categoria Mirim')
elif idade <= 14:
    print('Categoria Infantil')
elif idade <= 19:
    print('Categoria Junior')
elif idade <= 20:
    print('Categoria Sênior')
else:
    idade > 25
    print('Categoria Master')