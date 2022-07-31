import psycopg2

conexion = psycopg2.connect( user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db'
    )
try:
    with conexion:
        with conexion.cursor() as cursor:
        ##cursor = conexion.cursor()#crear un objeto del tipo cursos
            sentencia = 'SELECT * FROM persona' ##sentencia que se quiere ejecutar
            cursor.execute(sentencia)##mandar a llamar el metodo execute con ayuda del objeto cursor
            registros = cursor.fetchall()##recuperar todos los registros con fetchall
            print(registros)##imprimir
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()



cursor.close()##cerrar cursos
conexion.close()##cerrar conexion
