import psycopg2
#Actualizar un registro
conexion = psycopg2.connect( user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db'
    )
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s' #codigo para eliminar un id(registro)
            entrada = input('Proporciona los id_persona a elimimar (separados por coma): ')
            valores = (tuple(entrada.split(',')) ,) #(registro eliminar de id_persona)
            cursor.execute(sentencia, valores) ##se llamada de nuevo a executemany
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()



cursor.close()##cerrar cursos
conexion.close()##cerrar conexion
