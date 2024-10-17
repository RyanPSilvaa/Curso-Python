cidade = str(input('Digite o nome da cidade:'))
print(cidade[:5] == 'Santo')

###############################################

cidade = str(input('Digite o nome da cidade:')).strip()
print(cidade[:5].upper() == 'SANTO')