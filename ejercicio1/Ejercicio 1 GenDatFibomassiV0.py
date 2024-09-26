import os
import csv
import json
from datetime import datetime

# Serie Fibomassi
def generar_fibomassi(n):
    fibomassi = [0, 1]
    for i in range(2, n):
        fibomassi.append((fibomassi[i-1] + fibomassi[i-2]) * 1.1)
    return fibomassi

# Fecha y hora actual de nuestro sistema
def obtener_fecha_hora():
    now = datetime.now()
    fecha = now.strftime("%Y-%m-%d")
    hora = now.strftime("%H:%M:%S")
    return fecha, hora

# Guardar archivos en formatos TXT, CSV, JSON
def guardar_archivo(nombre_archivo, n, formato):
    fibomassi = generar_fibomassi(n)
    fecha, hora = obtener_fecha_hora()

    # Estructura de las columnas: N°, Fecha, Hora, Serie Fibomassi
    if formato == 'txt':
        with open(nombre_archivo, 'w') as archivo:
            archivo.write('N°\tFecha\tHora\tSerie Fibomassi\n')
            archivo.write('---\t----------\t--------\t----------------\n')
            for i, valor in enumerate(fibomassi):
                archivo.write(f"{i+1}\t{fecha}\t{hora}\t{valor:.2f}\n")
        print(f"Archivo TXT '{nombre_archivo}' generado.")

    elif formato == 'csv':
        with open(nombre_archivo, 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(['N°', 'Fecha', 'Hora', 'Serie Fibomassi'])
            for i, valor in enumerate(fibomassi):
                writer.writerow([i+1, fecha, hora, f"{valor:.2f}"])
        print(f"Archivo CSV '{nombre_archivo}' generado.")

    elif formato == 'json':
        datos = [{"N°": i+1, "Fecha": fecha, "Hora": hora, "Serie Fibomassi": round(valor, 2)} for i, valor in enumerate(fibomassi)]
        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)
        print(f"Archivo JSON '{nombre_archivo}' generado.")

# Menú
def menu():
    while True:
        try:
            num_series = int(input("¿Cuántas series de 35 elementos de la serie Fibomassi desea generar?: "))
            if num_series <= 0:
                raise ValueError("El número debe ser positivo.")
            n = 35  # Número fijo de elementos en cada serie
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, intente de nuevo.")
    
    while True:
        print("\n--- Menú de Generación de Archivos ---")
        print("1. Generar archivo TXT")
        print("2. Generar archivo CSV")
        print("3. Generar archivo JSON")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion in ['1', '2', '3']:
            formato = {'1': 'txt', '2': 'csv', '3': 'json'}[opcion]
            for i in range(1, num_series + 1):
                nombre_archivo = input(f"Ingrese el nombre base para los archivos {formato.upper()} (sin extensión): ")
                nombre_archivo_completo = f"{nombre_archivo}_{i}.{formato}"
                guardar_archivo(nombre_archivo_completo, n, formato)
        elif opcion == '4':
            print("Hasta luego.")
            break
        else:
            print("Opción inválida, intente de nuevo.")

# Ejecutar el menú
menu()
