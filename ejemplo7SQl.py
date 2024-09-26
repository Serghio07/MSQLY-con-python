import mysql.connector
import tkinter as tk
from tkinter import messagebox, simpledialog

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="sergio",  # usa tu nombre como el usuario de la base de datos
    database="ticona"
)
cursor = conexion.cursor()

# Función para agregar un artículo
def agregar_articulo():
    nombre = simpledialog.askstring("Agregar artículo", "Nombre del artículo:")
    descripcion = simpledialog.askstring("Agregar artículo", "Descripción del artículo:")
    precio = simpledialog.askfloat("Agregar artículo", "Precio del artículo:")
    if nombre and descripcion and precio is not None:
        sql = "INSERT INTO mamani (nombre_articulo, descripcion_articulo, precio) VALUES (%s, %s, %s)"
        valores = (nombre, descripcion, precio)
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Artículo agregado correctamente.")
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios.")

# Función para borrar un artículo
def borrar_articulo():
    id_articulo = simpledialog.askstring("Borrar artículo", "ID del artículo a borrar:")
    if id_articulo:
        sql = "DELETE FROM mamani WHERE id = %s"
        cursor.execute(sql, (id_articulo,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Artículo borrado correctamente.")
    else:
        messagebox.showwarning("Error", "Debes ingresar el ID del artículo.")

# Función para modificar un artículo
def modificar_articulo():
    id_articulo = simpledialog.askstring("Modificar artículo", "ID del artículo a modificar:")
    nombre = simpledialog.askstring("Modificar artículo", "Nuevo nombre del artículo:")
    descripcion = simpledialog.askstring("Modificar artículo", "Nueva descripción del artículo:")
    precio = simpledialog.askfloat("Modificar artículo", "Nuevo precio del artículo:")
    if id_articulo and nombre and descripcion and precio is not None:
        sql = "UPDATE mamani SET nombre_articulo = %s, descripcion_articulo = %s, precio = %s WHERE id = %s"
        valores = (nombre, descripcion, precio, id_articulo)
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Artículo modificado correctamente.")
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios.")

# Función para listar todos los artículos
def listar_articulos():
    cursor.execute("SELECT * FROM mamani")
    resultados = cursor.fetchall()
    listado = ""
    for articulo in resultados:
        listado += f"ID: {articulo[0]}, Nombre: {articulo[1]}, Descripción: {articulo[2]}, Precio: {articulo[3]}\n"
    
    messagebox.showinfo("Listado de artículos", listado)

# Función para generar un reporte en un archivo de texto
def generar_reporte():
    cursor.execute("SELECT * FROM mamani")
    resultados = cursor.fetchall()
    with open("reporte_articulos.txt", "w") as archivo:
        for articulo in resultados:
            archivo.write(f"ID: {articulo[0]}, Nombre: {articulo[1]}, Descripción: {articulo[2]}, Precio: {articulo[3]}\n")
    messagebox.showinfo("Éxito", "Reporte generado correctamente en 'reporte_articulos.txt'.")

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("ABMC Artículos")
ventana.geometry("300x250")

# Crear los botones del menú
boton_agregar = tk.Button(ventana, text="Agregar artículo", command=agregar_articulo)
boton_agregar.pack(pady=10)

boton_borrar = tk.Button(ventana, text="Borrar artículo", command=borrar_articulo)
boton_borrar.pack(pady=10)

boton_modificar = tk.Button(ventana, text="Modificar artículo", command=modificar_articulo)
boton_modificar.pack(pady=10)

boton_listar = tk.Button(ventana, text="Listar artículos", command=listar_articulos)
boton_listar.pack(pady=10)

boton_reporte = tk.Button(ventana, text="Generar reporte", command=generar_reporte)
boton_reporte.pack(pady=10)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=10)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()

# Cerrar la conexión a la base de datos al cerrar la ventana
cursor.close()
conexion.close()
