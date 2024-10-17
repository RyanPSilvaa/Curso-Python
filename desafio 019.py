import random
var1 = str(input('Digite um nome:'))
var2 = str(input('Digite um nome:'))
var3 = str(input('Digite um nome:'))
var4 = str(input('Digite um nome:'))
lista = [var1, var2, var3, var4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))