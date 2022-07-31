import psycopg2

conexion = psycopg2.connect( user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db'
    )
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = (
                ('Sonia','Alcantara','sonca@gmail.com'),
                ('Francisco', 'Escamilla', 'frcos@gmail.com'),
                ('Martin', 'Santiago', 'sigjed@gmail.com'),
            )
            cursor.executemany(sentencia, valores) #executemany para varios registros
            #conexion.commit()#commit guardara los cambios en la base de datos
            ##Al usar with, el commit se ejecuta automático, así que no hay que colocarse manuelmente
            registros_insertados = cursor.rowcount #rowcount nos dice cuantos registros se han incertado
            print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()



cursor.close()##cerrar cursos
conexion.close()##cerrar conexion
