nome = str(input('Digite seu nome completo:')).strip()

print('Analisando o seu nome:')
print('Seu nome em Maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em Minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu Primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))