import mysql.connector
# actualizando registros de python a mysql
personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='registros'
)
cursor = personas_db.cursor()
update_sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
valores = ('Louis','Loan',90,2)
cursor.execute(update_sql,valores)
personas_db.commit()

print(f'Se ha modificado la información')
cursor.close()
personas_db.close()