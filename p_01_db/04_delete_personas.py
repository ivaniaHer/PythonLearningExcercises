import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='registros'
)
cursor = personas_db.cursor()

delete_sql  = 'DELETE from personas WHERE id=%s'
valores = (3,)
cursor.execute(delete_sql,valores)
personas_db.commit()

print(f'El registro se ha eliminado')
cursor.close()
personas_db.close()