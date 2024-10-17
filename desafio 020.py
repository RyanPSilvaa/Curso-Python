import random
var1 = str(input('Digite um nome:'))
var2 = str(input('Digite um nome:'))
var3 = str(input('Digite um nome:'))
var4 = str(input('Digite um nome:'))
lista = [var1, var2, var3, var4]
random.shuffle(lista)
print('A ordem de apresentação será')
print(lista)