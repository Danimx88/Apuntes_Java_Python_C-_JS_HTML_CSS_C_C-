import psycopg2

conexion = psycopg2.connect( user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db'
    )
try:
    with conexion:
        with conexion.cursor() as cursor:
        ##cursor = conexion.cursor()#crear un objeto del tipo cursos
            sentencia = 'SELECT * FROM persona WHERE id_persona IN (1,2)'
            #id_persona = input('Proporciona el valor de id_persona: ') ##ya se se pondran los valores en sentencia, no se requiere que el usuario los ingrese
            cursor.execute(sentencia)                                      #(sentencia, (id_persona,))
            registros = cursor.fetchall() ##Se selecciona de nuevo fetchall ya que será más de un registro
            for registros in registros: #se genera un for para los registros 
                print(registros)
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()



cursor.close()##cerrar cursos
conexion.close()##cerrar conexion
