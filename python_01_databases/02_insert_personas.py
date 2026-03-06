# INSERTAR REGISTROS DE PYTHON A SQL
import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='registros'
)

cursor = personas_db.cursor()

insert_sql = 'INSERT INTO personas(nombre, apellido, edad) VALUES(%s,%s,%s)'
valores = ('Meu','Hernandez', 3)
cursor.execute(insert_sql,valores)
personas_db.commit()
print(f'Se ha agregado el registro')
personas_db.close()
cursor.close()