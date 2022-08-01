print('Dibujar pino de navidad')
size = int(input('Introduzca el tamaño del pino: '))
n = 0;
print(f'El tamaño del pino es: {size} y el valor de n es {n}')

#Primer bucle, range(start,stop,step)

for i in range(1,size,2):
    print(('^'*i).center(size+12))

for leg in range(3):
    print(('|||').center(size+12))
print(('\_____/').center(size+12))
