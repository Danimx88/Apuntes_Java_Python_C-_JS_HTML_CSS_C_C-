import psycopg2
#Actualizar un registro
conexion = psycopg2.connect( user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db'
    )
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s' #codigo duro
            valores = ('Juan Carlos', 'Juarez', 'jcsh@gmail.com', 12) #valores a incertar así como numero de id del usuario que se va actualizar, en este caso al 12
            cursor.execute(sentencia, valores) #ejecuta sentencia y toma los valores para modificar la base
            registros_actualizdos = cursor.rowcount #dime cuantos registros se actualizaron
            print(f'Registros insertados: {registros_actualizdos}') #imprime los numeros de registros que se actualizaron
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()



cursor.close()##cerrar cursos
conexion.close()##cerrar conexion
