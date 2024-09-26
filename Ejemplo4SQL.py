import mysql.connector
conexion1=mysql.connector.connect(host="192.168.43.138", 
                                  user="brandon", 
                                  passwd="", 
                                  database="bd1")
cursor1=conexion1.cursor()
cursor1.execute("select codigo, descripcion, precio from articulos")
for fila in cursor1:
    print(fila)
conexion1.close()    
