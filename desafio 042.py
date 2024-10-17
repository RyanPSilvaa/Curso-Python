print('=-='*10)
print('Analisador de triângulos')
print('=-='*10)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 == r2 == r3:
    print('Os segmentos acima PODEM FORMAR um triângulo Equilátero.')
elif r1 == r2 != r3 != r1:
    print('Os segmentos acima PODEM FORMAR um triângulo Isóceles.')
else:
    print('Os segmentos acima PODEM FORMAR um triângulo Escaleno.')