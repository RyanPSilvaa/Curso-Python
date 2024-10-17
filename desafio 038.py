valor1 = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor:'))

if valor1 > valor2:
    print('O valor {} é maior que o valor {}'.format(valor1, valor2))
elif valor2 > valor1:
    print('O valor {} é maior que o valor {}'.format(valor2, valor1))
elif valor1 == valor2:
    print('O valor {} é igual ao valor {}'.format(valor1, valor2))
else:
    print('Por favor, Digite um número!')