#cores no terminal

#print('\033[0;31;44mOlá, Mundo!\033[m')

nome = 'Ryan'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}
print('Olá, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))