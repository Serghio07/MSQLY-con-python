import os
import csv
import math
from datetime import datetime
import matplotlib.pyplot as plt

nnn = 0
nombre_archivo = "resultado.csv"  # Variable global para nombre de archivo


# Funciones de aproximación de Taylor
def aproximacionCOS(nn, xx):
    suma = 0.0
    for kk in range(0, nn + 1):
        termino = (-1) ** kk * xx ** (2 * kk) / math.factorial(2 * kk)
        suma += termino
    return suma

def aproximacionEXP(nn, xx):
    suma = 0.0
    for kk in range(0, nn + 1):
        termino = xx ** kk / math.factorial(kk)
        suma += termino
    return suma

def aproximacionSEN(nn, xx):
    suma = 0.0
    for kk in range(0, nn + 1):
        termino = (-1) ** kk * xx ** (2 * kk + 1) / math.factorial(2 * kk + 1)
        suma += termino
    return suma

def aproximacionLOG(nn, xx):
    if xx <= -1:
        raise ValueError("El valor de xx debe ser mayor que -1 para la serie de Taylor del logaritmo natural.")
    suma = 0.0
    for kk in range(1, nn + 1):
        termino = (-1) ** (kk + 1) * xx ** kk / kk
        suma += termino
    return suma

def aproximacionINV(nn, xx):
    if xx >= 1:
        raise ValueError("El valor de xx debe ser menor que 1 para la serie de Taylor de 1/(1-x).")
    suma = 0.0
    for kk in range(0, nn + 1):
        termino = xx ** kk
        suma += termino
    return suma

def aproximacionBINOMIAL(nn, xx, kk):
    suma = 0.0
    for nn in range(0, nn + 1):
        termino = math.comb(kk, nn) * xx ** nn
        suma += termino
    return suma

def aproximacionARCTAN(nn, xx):
    suma = 0.0
    for kk in range(0, nn + 1):
        termino = (-1) ** kk * xx ** (2 * kk + 1) / (2 * kk + 1)
        suma += termino
    return suma


# Funciones para operaciones sobre el archivo CSV
def crear_archivo_csv(nombre_archivo):
    """Crea un archivo CSV y escribe los encabezados."""
    with open(nombre_archivo, 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['N', 'Aprox. Taylor', 'Valor Real', 'Error', 'Fecha', 'Hora'])  # Escribir encabezado
    print(f"Archivo '{nombre_archivo}' creado con datos iniciales.")


def agregar_datos_csv(nombre_archivo, ntaylor, funcion):
    global nnn
    """Agrega datos al archivo CSV usando la serie de Taylor seleccionada."""
    with open(nombre_archivo, 'a', newline='') as archivo:
        writer = csv.writer(archivo)
        for x in range(0, 360):
            x_rad = math.radians(x)
            try:
                if funcion == "cos":
                    aprox_T = aproximacionCOS(ntaylor, x_rad)
                    valor_real = math.cos(x_rad)
                elif funcion == "sen":
                    aprox_T = aproximacionSEN(ntaylor, x_rad)
                    valor_real = math.sin(x_rad)
                elif funcion == "exp":
                    aprox_T = aproximacionEXP(ntaylor, x_rad)
                    valor_real = math.exp(x_rad)
                elif funcion == "log":
                    if x_rad <= 0:
                        continue  # Evitar logaritmos indefinidos
                    aprox_T = aproximacionLOG(ntaylor, x_rad)
                    valor_real = math.log(1 + x_rad)
                elif funcion == "inv":
                    if x_rad >= 1:
                        continue  # Evitar divisiones por cero
                    aprox_T = aproximacionINV(ntaylor, x_rad)
                    valor_real = 1 / (1 - x_rad)
                elif funcion == "arctan":
                    aprox_T = aproximacionARCTAN(ntaylor, x_rad)
                    valor_real = math.atan(x_rad)
                else:
                    print("Función no válida.")
                    return

                error = math.fabs(aprox_T - valor_real)
                print(aprox_T, valor_real, error)
                fecha_actual = datetime.now().strftime("%Y-%m-%d")
                hora_actual = datetime.now().strftime("%H:%M:%S")
                writer.writerow([nnn, aprox_T, valor_real, error, fecha_actual, hora_actual])
                nnn += 1
            except Exception as e:
                print(f"Error al procesar el valor {x}: {e}")


def mostrar_datos_csv(nombre_archivo):
    """Muestra el contenido del archivo CSV."""
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r', newline='') as archivo:
            reader = csv.reader(archivo)
            print("\nContenido del archivo:")
            for linea in reader:
                print(', '.join(linea))
    else:
        print(f"El archivo '{nombre_archivo}' no existe.")


def graficar_csv(nombre_archivo):
    """Grafica los datos del archivo CSV."""
    if os.path.exists(nombre_archivo):
        n_values = []
        aprox_taylor_values = []
        valor_real_values = []
        error_values = []

        with open(nombre_archivo, 'r', newline='') as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                n_values.append(int(fila['N']))
                aprox_taylor_values.append(float(fila['Aprox. Taylor']))
                valor_real_values.append(float(fila['Valor Real']))
                error_values.append(float(fila['Error']))

        plt.figure()
        plt.plot(n_values, aprox_taylor_values, label="Aprox. Taylor")
        plt.plot(n_values, valor_real_values, label="Valor Real")
        plt.plot(n_values, error_values, label="Error")
        plt.xlabel("N")
        plt.ylabel("Valores")
        plt.title("Gráfica de Aprox. Taylor, Valor Real y Error")
        plt.legend()
        plt.grid(True)
        plt.show()

    else:
        print(f"El archivo '{nombre_archivo}' no existe.")


# Menú interactivo
def menu():
    cantn = 1  # Valor por defecto de Taylor
    funcion = "cos"  # Función por defecto
    while True:
        print("\n--- Menú de Operaciones con Archivos CSV ---")
        print("0. Nombre Archivo CSV")
        print("1. Crear archivo CSV")
        print("2. Agregar datos")
        print("3. Seleccionar función (cos, sen, exp, log, inv, arctan)")
        print("4. N de Taylor = 3")
        print("5. N de Taylor = 5")
        print("6. N de Taylor = 7")
        print("7. N de Taylor = 10")
        print("8. Mostrar datos")
        print("9. Graficar Datos")
        print("10. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '0':
            global nombre_archivo
            nombre_archivo = input("Ingrese el nombre del archivo CSV (con extensión .csv): ")
        elif opcion == '1':
            crear_archivo_csv(nombre_archivo)
        elif opcion == '2':
            agregar_datos_csv(nombre_archivo, cantn, funcion)
            print(f"Datos agregados para la función {funcion} con N de Taylor = {cantn}")
        elif opcion == '3':
            funcion = input("Ingrese la función a usar (cos, sen, exp, log, inv, arctan): ").lower()
            if funcion not in ["cos", "sen", "exp", "log", "inv", "arctan"]:
                print("Función no válida. Por favor, elija una de las opciones válidas.")
                funcion = "cos"  # Restablecer valor por defecto
        elif opcion == '4':
            cantn = 3
        elif opcion == '5':
            cantn = 5
        elif opcion == '6':
            cantn = 7
        elif opcion == '7':
            cantn = 10
        elif opcion == '8':
            mostrar_datos_csv(nombre_archivo)
        elif opcion == '9':
            graficar_csv(nombre_archivo)
        elif opcion == '10':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# Ejecutar el menú
menu()
