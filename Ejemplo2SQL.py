import mysql.connector
conexion1=mysql.connector.connect(host="172.18.2.57", 
                                  user="ruddy", 
                                  passwd="", 
                                  database="db1")
cursor1=conexion1.cursor()
cursor1.execute("show tables")
for tabla in cursor1:
    print(tabla)
conexion1.close()    
