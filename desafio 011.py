alt = float(input('altura da parede:'))
larg = float(input('largura da parede:'))
area = larg * alt
print('Sua parede tem a dimensão de  {}x{} e sua área é de {}M^2.'.format(larg, alt,area))
tinta = area/2
print('Para pintar a sua parede você vai precisar de {}L de tinta.'.format(tinta))