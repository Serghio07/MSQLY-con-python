import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="sergio",  # usa tu nombre como el usuario de la base de datos
    database="ticona"
)
cursor = conexion.cursor()

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú ABMC Artículos ---")
    print("1. Agregar artículo")
    print("2. Borrar artículo")
    print("3. Modificar artículo")
    print("4. Listar artículos")
    print("5. Generar reporte")
    print("6. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion

# Función para agregar un artículo
def agregar_articulo():
    nombre = input("Nombre del artículo: ")
    descripcion = input("Descripción del artículo: ")
    precio = float(input("Precio del artículo: "))
    sql = "INSERT INTO mamani (nombre_articulo, descripcion_articulo, precio) VALUES (%s, %s, %s)"
    valores = (nombre, descripcion, precio)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Artículo agregado correctamente.")

# Función para borrar un artículo
def borrar_articulo():
    id_articulo = input("ID del artículo a borrar: ")
    sql = "DELETE FROM mamani WHERE id = %s"
    cursor.execute(sql, (id_articulo,))
    conexion.commit()
    print("Artículo borrado correctamente.")

# Función para modificar un artículo
def modificar_articulo():
    id_articulo = input("ID del artículo a modificar: ")
    nombre = input("Nuevo nombre del artículo: ")
    descripcion = input("Nueva descripción del artículo: ")
    precio = float(input("Nuevo precio del artículo: "))
    sql = "UPDATE mamani SET nombre_articulo = %s, descripcion_articulo = %s, precio = %s WHERE id = %s"
    valores = (nombre, descripcion, precio, id_articulo)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Artículo modificado correctamente.")

# Función para listar todos los artículos
def listar_articulos():
    cursor.execute("SELECT * FROM mamani")
    resultados = cursor.fetchall()
    for articulo in resultados:
        print(f"ID: {articulo[0]}, Nombre: {articulo[1]}, Descripción: {articulo[2]}, Precio: {articulo[3]}")

# Función para generar un reporte en un archivo de texto
def generar_reporte():
    cursor.execute("SELECT * FROM mamani")
    resultados = cursor.fetchall()
    with open("reporte_articulos.txt", "w") as archivo:
        for articulo in resultados:
            archivo.write(f"ID: {articulo[0]}, Nombre: {articulo[1]}, Descripción: {articulo[2]}, Precio: {articulo[3]}\n")
    print("Reporte generado correctamente en 'reporte_articulos.txt'.")

# Bucle principal del menú
while True:
    opcion = mostrar_menu()
    
    if opcion == "1":
        agregar_articulo()
    elif opcion == "2":
        borrar_articulo()
    elif opcion == "3":
        modificar_articulo()
    elif opcion == "4":
        listar_articulos()
    elif opcion == "5":
        generar_reporte()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")

# Cerrar la conexión a la base de datos
cursor.close()
conexion.close()
