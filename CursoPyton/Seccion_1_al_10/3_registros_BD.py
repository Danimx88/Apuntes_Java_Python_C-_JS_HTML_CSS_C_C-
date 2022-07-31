import psycopg2

conexion = psycopg2.connect( user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db'
    )
try:
    with conexion:
        with conexion.cursor() as cursor:
        ##cursor = conexion.cursor()#crear un objeto del tipo cursos
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            llaves_primarias = ((1,2,3),)
            #id_persona = input('Proporciona el valor de id_persona: ')
            cursor.execute(sentencia, llaves_primarias)                                      #(sentencia, (id_persona,))
            registros = cursor.fetchall()
            for registros in registros:
                print(registros)
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()



cursor.close()##cerrar cursos
conexion.close()##cerrar conexion
