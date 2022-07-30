#for i in range(6):
#    if i % 2 == 0:
#        print(f'Valor : {i}')

for i in range(6):
    if i % 2 != 0: ##Si es un numero impar
        continue ##continuo que se vaya a la siguiente iteracion
    print(f'Valor {i}')
