import psycopg2 as bd
#Actualizar un registro
conexion = bd.connect( user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db'
    )
try:
        conexion.autocommit = False
        cursor = conexion.cursor()
        sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
        valores = ('Maria','Esparza','meparza@gmail.com')
        cursor.execute(sentencia, valores)
        conexion.commit()
        print('Termina la transacción ')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()



cursor.close()##cerrar cursos
conexion.close()##cerrar conexion
