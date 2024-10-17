nome = str(input('Digite um nome:'))
if nome == 'Ryan':
    print('Nome bonito!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Nome comum')
elif nome in 'Ana Júlia Ferreira':
    print('Belo nome feminino')
else:
    print('Seu nome é normal :)!')
print('Tenha um bom dia {}'.format(nome))