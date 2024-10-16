dias = int(input('Quantos dias de alugado?'))
km = float(input('Quantos KM rodados?'))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é R${:.2f}'.format(pago))