import csv
import json
from datetime import datetime

def generar_fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:n]

def crear_archivo_txt(nombre_archivo, num_series, datos_por_serie):
    fecha_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    contador_global = 1  
    with open(nombre_archivo, 'w') as archivo:
        archivo.write('Serie,N°,Fecha y Hora,Valor de Fibonacci\n')
        for serie in range(1, num_series + 1):
            fibonacci = generar_fibonacci(datos_por_serie)
            for valor in fibonacci:
                archivo.write(f'{serie},{contador_global},{fecha_hora},{valor}\n')
                contador_global += 1
    print(f"Archivo '{nombre_archivo}' creado con las series Fibonacci.")

def crear_archivo_csv(nombre_archivo, num_series, datos_por_serie):
    fecha_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    contador_global = 1 
    with open(nombre_archivo, 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['Serie', 'N°', 'Fecha y Hora', 'Valor de Fibonacci'])
        for serie in range(1, num_series + 1):
            fibonacci = generar_fibonacci(datos_por_serie)
            for valor in fibonacci:
                writer.writerow([serie, contador_global, fecha_hora, valor])
                contador_global += 1 
    print(f"Archivo '{nombre_archivo}' creado con las series Fibonacci.")

def crear_archivo_json(nombre_archivo, num_series, datos_por_serie):
    fecha_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    datos = []
    contador_global = 1
    for serie in range(1, num_series + 1):
        fibonacci = generar_fibonacci(datos_por_serie)
        for valor in fibonacci:
            datos.append({"Serie": serie, "N°": contador_global, "Fecha y Hora": fecha_hora, "Valor de Fibonacci": valor})
            contador_global += 1 
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    print(f"Archivo '{nombre_archivo}' creado con las series Fibonacci.")

def menu():
    nombre_archivo = input("Ingrese el nombre del archivo (sin extensión): ")
    num_series = int(input("Ingrese la cantidad de series Fibonacci a generar: "))
    datos_por_serie = 35

    while True:
        print("\n--- Menú de Operaciones con Archivos Fibonacci ---")
        print("1. Crear archivo TXT")
        print("2. Crear archivo CSV")
        print("3. Crear archivo JSON")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            crear_archivo_txt(f"{nombre_archivo}.txt", num_series, datos_por_serie)
        elif opcion == '2':
            crear_archivo_csv(f"{nombre_archivo}.csv", num_series, datos_por_serie)
        elif opcion == '3':
            crear_archivo_json(f"{nombre_archivo}.json", num_series, datos_por_serie)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
