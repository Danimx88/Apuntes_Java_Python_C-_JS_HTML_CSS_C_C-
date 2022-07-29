edad = int(input('Proporciona tu edad: '))

fecha = None
if edad < 11:
    fecha = 'La infancia es increible'
elif edad < 20 or edad > 10:
    fecha = 'Muchos cambios o muchos estudios'
elif edad < 30 or edad > 20:
    fecha ='Muchos cambios o muchos estudios'
else:
    fecha = 'Etapa de vida no reconocida'

print(f'mes{edad} {fecha}')
