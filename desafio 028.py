from random import randint
comp = randint(0,100) # fazendo com o que o computador pense!
print('=-='*8)
print('Vou pensar num número de 0 a 100 tente adivinhar...')
print('=-='*8)
num = int(input('Em qual número eu pensei?'))
print('Loading..')
if num == comp:
    print('Isso mesmo, pensei no 0!')
else:
    print('Infelizmente você errou o número que eu pensei foi {}, quem sabe na próxima você acerte!'.format(comp))