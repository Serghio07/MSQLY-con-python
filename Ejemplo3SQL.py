import mysql.connector
conexion1=mysql.connector.connect(host="172.18.2.57", 
                                  user="ruddy", 
                                  passwd="", 
                                  database="db1")
cursor1=conexion1.cursor()
sql="insert into articulos(descripcion, precio) values (%s,%s)"
datos = ("manzana", 18.75)
cursor1.execute(sql, datos)

datos = ("naranja", 22)
cursor1.execute(sql, datos)

datos = ("banana", 19.50)
cursor1.execute(sql, datos)

datos = ("pera", 21.75)
cursor1.execute(sql, datos)

datos = ("fresas", 45)
cursor1.execute(sql, datos)

datos = ("piña", 30)
cursor1.execute(sql, datos)
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()    
