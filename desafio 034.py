salario = float(input('Digite o salário:'))
if salario <= 1412:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, novo))