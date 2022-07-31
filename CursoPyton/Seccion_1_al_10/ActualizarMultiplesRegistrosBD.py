import psycopg2
#Actualizar un registro
conexion = psycopg2.connect( user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db'
    )
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s'
            valores = (
                        ('Octavio', 'Olmeda', 'oldoct@gmail.com', 10),
                       ('Arturo', 'Sanchez', 'arsa@gmail.com', 11),
                       ('Rafael', 'Marquez', 'rafmr@gmail.com', 12)
                       )
            cursor.executemany(sentencia, valores) ##se llamada de nuevo a executemany
            registros_actualizdos = cursor.rowcount
            print(f'Registros insertados: {registros_actualizdos}')
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()



cursor.close()##cerrar cursos
conexion.close()##cerrar conexion
