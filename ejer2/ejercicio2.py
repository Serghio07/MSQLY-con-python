import csv
import json
import math
from datetime import datetime

def calcular_cos_taylor(x, n):
    # Serie de Taylor para coseno en torno a 0 (Maclaurin)
    cos_taylor = 0
    for i in range(n):
        coef = (-1)**i
        cos_taylor += coef * (x**(2*i)) / math.factorial(2*i)
    return cos_taylor

def crear_archivo_txt(nombre_archivo, n, max_valor_x):
    fecha_hora = datetime.now().strftime("%d-%m-%Y")
    with open(nombre_archivo, 'w') as archivo:
        archivo.write('N°,Fecha,Hora,Cos Taylor,Cos Trig,Error\n')
        for i in range(1, max_valor_x + 1):
            hora_actual = datetime.now().strftime("%H:%M:%S")
            x = i / 10.0  # Valores de x en incrementos de 0.1
            cos_taylor = calcular_cos_taylor(x, min(n, 20))  # Limitar la serie a 20 términos
            cos_trig = math.cos(x)
            error = abs(cos_taylor - cos_trig)
            archivo.write(f'{i},{fecha_hora},{hora_actual},{cos_taylor},{cos_trig},{error}\n')
    print(f"Archivo '{nombre_archivo}' creado con la serie de Taylor para coseno.")

def crear_archivo_csv(nombre_archivo, n, max_valor_x):
    fecha_hora = datetime.now().strftime("%d-%m-%Y")
    with open(nombre_archivo, 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['N°', 'Fecha', 'Hora', 'Cos Taylor', 'Cos Trig', 'Error'])
        for i in range(1, max_valor_x + 1):
            hora_actual = datetime.now().strftime("%H:%M:%S")
            x = i / 10.0  # Valores de x en incrementos de 0.1
            cos_taylor = calcular_cos_taylor(x, min(n, 20))  # Limitar la serie a 20 términos
            cos_trig = math.cos(x)
            error = abs(cos_taylor - cos_trig)
            writer.writerow([i, fecha_hora, hora_actual, cos_taylor, cos_trig, error])
    print(f"Archivo '{nombre_archivo}' creado con la serie de Taylor para coseno.")

def crear_archivo_json(nombre_archivo, n, max_valor_x):
    fecha_hora = datetime.now().strftime("%d-%m-%Y")
    datos = []
    for i in range(1, max_valor_x + 1):
        hora_actual = datetime.now().strftime("%H:%M:%S")
        x = i / 10.0  # Valores de x en incrementos de 0.1
        cos_taylor = calcular_cos_taylor(x, min(n, 20))  # Limitar la serie a 20 términos
        cos_trig = math.cos(x)
        error = abs(cos_taylor - cos_trig)
        datos.append({"N°": i, "Fecha": fecha_hora, "Hora": hora_actual, "Cos Taylor": cos_taylor, "Cos Trig": cos_trig, "Error": error})
    
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    print(f"Archivo '{nombre_archivo}' creado con la serie de Taylor para coseno.")

def menu():
    nombre_archivo = input("Ingrese el nombre del archivo (sin extensión): ")
    n = int(input("Ingrese el número de términos para la serie de Taylor (n): "))
    max_valor_x = 100  # Se generan 100 puntos de datos (de 0.1 a 10.0)

    while True:
        print("\n--- Menú de Operaciones con la Serie de Taylor para Coseno ---")
        print("1. Crear archivo TXT")
        print("2. Crear archivo CSV")
        print("3. Crear archivo JSON")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            crear_archivo_txt(f"{nombre_archivo}.txt", n, max_valor_x)
        elif opcion == '2':
            crear_archivo_csv(f"{nombre_archivo}.csv", n, max_valor_x)
        elif opcion == '3':
            crear_archivo_json(f"{nombre_archivo}.json", n, max_valor_x)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()

