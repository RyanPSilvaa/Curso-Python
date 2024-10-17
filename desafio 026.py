frase = str(input('Digite uma Frase:')).strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('a  letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('a  letra A apareceu  na posição {}.'.format(frase.rfind('A')+1))