def mi_Funcion(nombre, apellido):
    print('saludos desde mi funcion')
    print(f'Nombre: {nombre}, Apellido: {apellido}')

def mi_Funcion2(x, y):
    d = x + y
    print(d)

name = input('Introduzca su nombre: ')
lastname = input('Introduzca su appelido: ')
mi_Funcion(name, lastname)

x = int(input('Introduzca valor de x: '))
y = int(input('Introduzca valor de y: '))
mi_Funcion2(x, y)
