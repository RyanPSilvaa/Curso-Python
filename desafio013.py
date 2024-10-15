salario = float(input('Qual é o salário do Funcionário?'))
novo = salario + (salario * 15/100)
print('O salário que o funcionário ganhava era de R${:.2f}, com 15% de aumento, passa a ser R${:.2f}'.format(salario, novo))