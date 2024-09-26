import os
import csv
import time
import math
from datetime import datetime
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt

nnn = 0

# Función de aproximación de Taylor para el COS
def aproximacionCOS(nn, xx):
    suma = 0.0
    for kk in range(0, nn + 1):
        termino = (-1) ** kk * xx ** (2 * kk) / math.factorial(2 * kk)
        suma += termino
    return suma
# Función de aproximación de Taylor para la exponencial
def aproximacionEXP(nn, xx):
    suma = 0.0
    for kk in range(0, nn + 1):
        termino = xx ** kk / math.factorial(kk)
        suma += termino
    return suma
# Función de aproximación de Taylor para el SENO
def aproximacionSEN(nn, xx):
    suma = 0.0
    for kk in range(0, nn + 1):
        termino = (-1) ** kk * xx ** (2 * kk + 1) / math.factorial(2 * kk + 1)
        suma += termino
    return suma
# Función de aproximación de Taylor para el LOGARITMO NATURAL
def aproximacionLOG(nn, xx):
    if xx <= -1:
        raise ValueError("El valor de xx debe ser mayor que -1 para la serie de Taylor del logaritmo natural.")
    suma = 0.0
    for kk in range(1, nn + 1):
        termino = (-1) ** (kk + 1) * xx ** kk / kk
        suma += termino
    return suma
# Función de aproximación de Taylor para 1/(1-x)
def aproximacionINV(nn, xx):
    if xx >= 1:
        raise ValueError("El valor de xx debe ser menor que 1 para la serie de Taylor de 1/(1-x).")
    suma = 0.0
    for kk in range(0, nn + 1):
        termino = xx ** kk
        suma += termino
    return suma
# Función de aproximación de Taylor para (1 + x)^k
def aproximacionBINOMIAL(nn, xx, kk):
    suma = 0.0
    for nn in range(0, nn + 1):
        termino = math.comb(kk, nn) * xx ** nn
        suma += termino
    return suma
# Función de aproximación de Taylor para arctan(x)
def aproximacionARCTAN(nn, xx):
    suma = 0.0
    for kk in range(0, nn + 1):
        termino = (-1) ** kk * xx ** (2 * kk + 1) / (2 * kk + 1)
        suma += termino
    return suma
# Funciones para las operaciones sobre el archivo CSV
def crear_archivo_csv(nombre_archivo):
    """Crea un archivo CSV y escribe datos iniciales."""
    with open(nombre_archivo, 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([
            'N', 
            'Cos Taylor', 'math.cos', 'Error Cos', 
            'Exp Taylor', 'math.exp', 'Error Exp', 
            'Sen Taylor', 'math.sin', 'Error Sen', 
            'Log Taylor', 'math.log', 'Error Log', 
            'Inv Taylor', '1/(1-x)', 'Error Inv', 
            'Binomial Taylor', '(1+x)^k', 'Error Binomial', 
            'Arctan Taylor', 'math.atan', 'Error Arctan', 
            'Fecha', 'Hora'
        ])  # Escribir encabezado
    messagebox.showinfo("Éxito", f"Archivo '{nombre_archivo}' creado con datos iniciales.")
def agregar_datos_csv(nombre_archivo, ntaylor):
    global nnn
    """Agrega una nueva línea de datos al archivo CSV."""
    with open(nombre_archivo, 'a', newline='') as archivo:
        writer = csv.writer(archivo)
        for x in range(0, 834):
            x_rad = math.radians(x)
            
            # Calcular valores usando las series de Taylor
            cos_T = aproximacionCOS(ntaylor, x_rad)
            exp_T = aproximacionEXP(ntaylor, x_rad)
            sen_T = aproximacionSEN(ntaylor, x_rad)
            
            # Asegurar que el valor de xx para log y inv esté en el rango adecuado
            log_xx = x_rad - 1 if x_rad - 1 > -1 else -0.999
            inv_xx = x_rad - 1 if x_rad - 1 < 1 else 0.999
            
            log_T = aproximacionLOG(ntaylor, log_xx)  # log(1 + x) -> x_rad - 1 para valores en el rango adecuado
            inv_T = aproximacionINV(ntaylor, inv_xx)  # 1/(1 - x) -> x_rad - 1 para valores en el rango adecuado
            binomial_T = aproximacionBINOMIAL(ntaylor, x_rad, 2)  # (1 + x)^2 como ejemplo
            arctan_T = aproximacionARCTAN(ntaylor, x_rad)
            
            # Calcular valores usando las funciones matemáticas de Python
            cos_M = math.cos(x_rad)
            exp_M = math.exp(x_rad)
            sen_M = math.sin(x_rad)
            log_M = math.log(x_rad) if x_rad > 0 else float('nan')  # Evitar log de valores no positivos
            inv_M = 1 / (1 - x_rad) if x_rad < 1 else float('nan')  # Evitar división por cero
            binomial_M = (1 + x_rad) ** 2
            arctan_M = math.atan(x_rad)
            
            # Calcular errores
            error_cos = math.fabs(cos_T - cos_M)
            error_exp = math.fabs(exp_T - exp_M)
            error_sen = math.fabs(sen_T - sen_M)
            error_log = math.fabs(log_T - log_M) if not math.isnan(log_M) else float('nan')
            error_inv = math.fabs(inv_T - inv_M) if not math.isnan(inv_M) else float('nan')
            error_binomial = math.fabs(binomial_T - binomial_M)
            error_arctan = math.fabs(arctan_T - arctan_M)
            
            # Obtener fecha y hora actuales
            fecha_actual = datetime.now().strftime("%Y-%m-%d")
            hora_actual = datetime.now().strftime("%H:%M:%S")
            
            # Escribir fila en el archivo CSV
            writer.writerow([
                nnn, 
                cos_T, cos_M, error_cos, 
                exp_T, exp_M, error_exp, 
                sen_T, sen_M, error_sen, 
                log_T, log_M, error_log, 
                inv_T, inv_M, error_inv, 
                binomial_T, binomial_M, error_binomial, 
                arctan_T, arctan_M, error_arctan, 
                fecha_actual, hora_actual
            ])
            nnn += 1
    messagebox.showinfo("Éxito", f"Datos agregados al archivo '{nombre_archivo}'.")

def mostrar_datos_csv(nombre_archivo):
    """Muestra el contenido del archivo CSV en una nueva ventana de Tkinter."""
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r', newline='') as archivo:
            reader = csv.reader(archivo)
            contenido = "\n".join([', '.join(linea) for linea in reader])
        
        # Crear una nueva ventana
        ventana_datos = tk.Toplevel(root)
        ventana_datos.title("Contenido del CSV")
        ventana_datos.geometry("600x400")
        
        # Crear un widget de texto para mostrar el contenido del archivo CSV
        texto_datos = tk.Text(ventana_datos, wrap=tk.WORD)
        texto_datos.insert(tk.END, contenido)
        texto_datos.config(state=tk.DISABLED)  # Hacer que el widget de texto sea de solo lectura
        texto_datos.pack(expand=True, fill=tk.BOTH)
    else:
        messagebox.showerror("Error", f"El archivo '{nombre_archivo}' no existe.")

def graficar_csv(nombre_archivo):
    if os.path.exists(nombre_archivo):
        n_values = []
        cos_taylor_values = []
        cos_math_values = []
        error_cos_values = []
        exp_taylor_values = []
        exp_math_values = []
        error_exp_values = []
        sen_taylor_values = []
        sen_math_values = []
        error_sen_values = []
        log_taylor_values = []
        log_math_values = []
        error_log_values = []
        inv_taylor_values = []
        inv_math_values = []
        error_inv_values = []
        binomial_taylor_values = []
        binomial_math_values = []
        error_binomial_values = []
        arctan_taylor_values = []
        arctan_math_values = []
        error_arctan_values = []

        # Leer el archivo CSV
        with open(nombre_archivo, 'r', newline='') as archivo:
            reader = csv.DictReader(archivo)

            for fila in reader:
                n_values.append(int(fila['N']))  # Columna N
                cos_taylor_values.append(float(fila['Cos Taylor']))  # Columna Cos Taylor
                cos_math_values.append(float(fila['math.cos']))  # Columna math.cos
                error_cos_values.append(float(fila['Error Cos']))  # Columna Error Cos
                exp_taylor_values.append(float(fila['Exp Taylor']))  # Columna Exp Taylor
                exp_math_values.append(float(fila['math.exp']))  # Columna math.exp
                error_exp_values.append(float(fila['Error Exp']))  # Columna Error Exp
                sen_taylor_values.append(float(fila['Sen Taylor']))  # Columna Sen Taylor
                sen_math_values.append(float(fila['math.sin']))  # Columna math.sin
                error_sen_values.append(float(fila['Error Sen']))  # Columna Error Sen
                log_taylor_values.append(float(fila['Log Taylor']))  # Columna Log Taylor
                log_math_values.append(float(fila['math.log']))  # Columna math.log
                error_log_values.append(float(fila['Error Log']))  # Columna Error Log
                inv_taylor_values.append(float(fila['Inv Taylor']))  # Columna Inv Taylor
                inv_math_values.append(float(fila['1/(1-x)']))  # Columna 1/(1-x)
                error_inv_values.append(float(fila['Error Inv']))  # Columna Error Inv
                binomial_taylor_values.append(float(fila['Binomial Taylor']))  # Columna Binomial Taylor
                binomial_math_values.append(float(fila['(1+x)^k']))  # Columna (1+x)^k
                error_binomial_values.append(float(fila['Error Binomial']))  # Columna Error Binomial
                arctan_taylor_values.append(float(fila['Arctan Taylor']))  # Columna Arctan Taylor
                arctan_math_values.append(float(fila['math.atan']))  # Columna math.atan
                error_arctan_values.append(float(fila['Error Arctan']))  # Columna Error Arctan

        # Graficar
        plt.figure(figsize=(12, 8))

        # Gráfica de Cos Taylor
        plt.subplot(3, 1, 1)
        plt.plot(n_values, cos_taylor_values, label="Cos Taylor")
        plt.plot(n_values, cos_math_values, label="math.cos")
        plt.plot(n_values, error_cos_values, label="Error Cos")
        plt.xlabel("N")
        plt.ylabel("Valores")
        plt.title("Gráfica de Cos Taylor, math.cos y Error Cos")
        plt.legend()
        plt.grid(True)

        # Gráfica de Exp Taylor
        plt.subplot(3, 1, 2)
        plt.plot(n_values, exp_taylor_values, label="Exp Taylor")
        plt.plot(n_values, exp_math_values, label="math.exp")
        plt.plot(n_values, error_exp_values, label="Error Exp")
        plt.xlabel("N")
        plt.ylabel("Valores")
        plt.title("Gráfica de Exp Taylor, math.exp y Error Exp")
        plt.legend()
        plt.grid(True)

        # Gráfica de Sen Taylor
        plt.subplot(3, 1, 3)
        plt.plot(n_values, sen_taylor_values, label="Sen Taylor")
        plt.plot(n_values, sen_math_values, label="math.sin")
        plt.plot(n_values, error_sen_values, label="Error Sen")
        plt.xlabel("N")
        plt.ylabel("Valores")
        plt.title("Gráfica de Sen Taylor, math.sin y Error Sen")
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

        # Graficar en una nueva figura para Log, Inv, Binomial y Arctan
        plt.figure(figsize=(12, 8))

        # Gráfica de Log Taylor
        plt.subplot(4, 1, 1)
        plt.plot(n_values, log_taylor_values, label="Log Taylor")
        plt.plot(n_values, log_math_values, label="math.log")
        plt.plot(n_values, error_log_values, label="Error Log")
        plt.xlabel("N")
        plt.ylabel("Valores")
        plt.title("Gráfica de Log Taylor, math.log y Error Log")
        plt.legend()
        plt.grid(True)

        # Gráfica de Inv Taylor
        plt.subplot(4, 1, 2)
        plt.plot(n_values, inv_taylor_values, label="Inv Taylor")
        plt.plot(n_values, inv_math_values, label="1/(1-x)")
        plt.plot(n_values, error_inv_values, label="Error Inv")
        plt.xlabel("N")
        plt.ylabel("Valores")
        plt.title("Gráfica de Inv Taylor, 1/(1-x) y Error Inv")
        plt.legend()
        plt.grid(True)

        # Gráfica de Binomial Taylor
        plt.subplot(4, 1, 3)
        plt.plot(n_values, binomial_taylor_values, label="Binomial Taylor")
        plt.plot(n_values, binomial_math_values, label="(1+x)^k")
        plt.plot(n_values, error_binomial_values, label="Error Binomial")
        plt.xlabel("N")
        plt.ylabel("Valores")
        plt.title("Gráfica de Binomial Taylor, (1+x)^k y Error Binomial")
        plt.legend()
        plt.grid(True)

        # Gráfica de Arctan Taylor
        plt.subplot(4, 1, 4)
        plt.plot(n_values, arctan_taylor_values, label="Arctan Taylor")
        plt.plot(n_values, arctan_math_values, label="math.atan")
        plt.plot(n_values, error_arctan_values, label="Error Arctan")
        plt.xlabel("N")
        plt.ylabel("Valores")
        plt.title("Gráfica de Arctan Taylor, math.atan y Error Arctan")
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    else:
        messagebox.showerror("Error", f"El archivo '{nombre_archivo}' no existe.")
def graficar_csv_errores(nombre_archivo_salida):
    """Grafica los valores y errores de cada serie del archivo CSV de salida para filas con errores > 0.1."""
    if os.path.exists(nombre_archivo_salida):
        # Inicializar listas para cada serie
        cos_data = {'n': [], 'taylor': [], 'math': [], 'error': []}
        exp_data = {'n': [], 'taylor': [], 'math': [], 'error': []}
        sen_data = {'n': [], 'taylor': [], 'math': [], 'error': []}
        log_data = {'n': [], 'taylor': [], 'math': [], 'error': []}
        inv_data = {'n': [], 'taylor': [], 'math': [], 'error': []}
        binomial_data = {'n': [], 'taylor': [], 'math': [], 'error': []}
        arctan_data = {'n': [], 'taylor': [], 'math': [], 'error': []}

        # Leer el archivo CSV de salida
        with open(nombre_archivo_salida, 'r', newline='') as archivo:
            reader = csv.DictReader(archivo)

            for fila in reader:
                n = int(fila['N'])

                # Serie Cos
                cos_data['n'].append(n)
                cos_data['taylor'].append(float(fila['Cos Taylor']))
                cos_data['math'].append(float(fila['math.cos']))
                cos_data['error'].append(float(fila['Error Cos']))

                # Serie Exp
                exp_data['n'].append(n)
                exp_data['taylor'].append(float(fila['Exp Taylor']))
                exp_data['math'].append(float(fila['math.exp']))
                exp_data['error'].append(float(fila['Error Exp']))

                # Serie Sen
                sen_data['n'].append(n)
                sen_data['taylor'].append(float(fila['Sen Taylor']))
                sen_data['math'].append(float(fila['math.sin']))
                sen_data['error'].append(float(fila['Error Sen']))

                # Serie Log
                log_data['n'].append(n)
                log_data['taylor'].append(float(fila['Log Taylor']))
                log_data['math'].append(float(fila['math.log']))
                log_data['error'].append(float(fila['Error Log']))

                # Serie Inv
                inv_data['n'].append(n)
                inv_data['taylor'].append(float(fila['Inv Taylor']))
                inv_data['math'].append(float(fila['1/(1-x)']))
                inv_data['error'].append(float(fila['Error Inv']))

                # Serie Binomial
                binomial_data['n'].append(n)
                binomial_data['taylor'].append(float(fila['Binomial Taylor']))
                binomial_data['math'].append(float(fila['(1+x)^k']))
                binomial_data['error'].append(float(fila['Error Binomial']))

                # Serie Arctan
                arctan_data['n'].append(n)
                arctan_data['taylor'].append(float(fila['Arctan Taylor']))
                arctan_data['math'].append(float(fila['math.atan']))
                arctan_data['error'].append(float(fila['Error Arctan']))

        # Filtrar filas con errores > 0.1
        def filtrar_errores(data):
            filtered_data = {'n': [], 'taylor': [], 'math': [], 'error': []}
            for i in range(len(data['n'])):
                if data['error'][i] > 0.1:
                    filtered_data['n'].append(data['n'][i])
                    filtered_data['taylor'].append(data['taylor'][i])
                    filtered_data['math'].append(data['math'][i])
                    filtered_data['error'].append(data['error'][i])
            return filtered_data

        filtered_cos_data = filtrar_errores(cos_data)
        filtered_exp_data = filtrar_errores(exp_data)
        filtered_sen_data = filtrar_errores(sen_data)
        filtered_log_data = filtrar_errores(log_data)
        filtered_inv_data = filtrar_errores(inv_data)
        filtered_binomial_data = filtrar_errores(binomial_data)
        filtered_arctan_data = filtrar_errores(arctan_data)

        # Graficar cada serie por separado
        def graficar_serie(data, titulo, taylor_label, math_label, error_label):
            plt.figure(figsize=(12, 6))
            plt.plot(data['n'], data['taylor'], label=taylor_label)
            plt.plot(data['n'], data['math'], label=math_label)
            plt.plot(data['n'], data['error'], label=error_label)
            plt.xlabel("N")
            plt.ylabel("Valores")
            plt.title(titulo)
            plt.legend()
            plt.grid(True)
            plt.show()

        graficar_serie(filtered_cos_data, "Gráfica de Cos Taylor, math.cos y Error Cos", "Cos Taylor", "math.cos", "Error Cos")
        graficar_serie(filtered_exp_data, "Gráfica de Exp Taylor, math.exp y Error Exp", "Exp Taylor", "math.exp", "Error Exp")
        graficar_serie(filtered_sen_data, "Gráfica de Sen Taylor, math.sin y Error Sen", "Sen Taylor", "math.sin", "Error Sen")
        graficar_serie(filtered_log_data, "Gráfica de Log Taylor, math.log y Error Log", "Log Taylor", "math.log", "Error Log")
        graficar_serie(filtered_inv_data, "Gráfica de Inv Taylor, 1/(1-x) y Error Inv", "Inv Taylor", "1/(1-x)", "Error Inv")
        graficar_serie(filtered_binomial_data, "Gráfica de Binomial Taylor, (1+x)^k y Error Binomial", "Binomial Taylor", "(1+x)^k", "Error Binomial")
        graficar_serie(filtered_arctan_data, "Gráfica de Arctan Taylor, math.atan y Error Arctan", "Arctan Taylor", "math.atan", "Error Arctan")

    else:
        messagebox.showerror("Error", f"El archivo '{nombre_archivo_salida}' no existe.")
# Función para calcular porcentajes de errores
def Porcentajes(nombre_archivo):
    if os.path.exists(nombre_archivo):
        error_cos_values = []
        error_exp_values = []
        error_sen_values = []
        error_log_values = []
        error_inv_values = []
        error_binomial_values = []
        error_arctan_values = []

        # Leer el archivo CSV
        with open(nombre_archivo, 'r', newline='') as archivo:
            reader = csv.DictReader(archivo)

            for fila in reader:
                error_cos_values.append(float(fila['Error Cos']))  # Columna Error Cos
                error_exp_values.append(float(fila['Error Exp']))  # Columna Error Exp
                error_sen_values.append(float(fila['Error Sen']))  # Columna Error Sen
                error_log_values.append(float(fila['Error Log']))  # Columna Error Log
                error_inv_values.append(float(fila['Error Inv']))  # Columna Error Inv
                error_binomial_values.append(float(fila['Error Binomial']))  # Columna Error Binomial
                error_arctan_values.append(float(fila['Error Arctan']))  # Columna Error Arctan

        # Función para calcular porcentajes
        def calcular_porcentajes(error_values):
            total = len(error_values)
            if total == 0:
                return (0, 0)
            superior_01 = sum(1 for error in error_values if error > 0.1) / total * 100
            menor_01 = sum(1 for error in error_values if error <= 0.1) / total * 100
            return (superior_01, menor_01)

        # Calcular porcentajes para cada serie
        porcentajes_cos = calcular_porcentajes(error_cos_values)
        porcentajes_exp = calcular_porcentajes(error_exp_values)
        porcentajes_sen = calcular_porcentajes(error_sen_values)
        porcentajes_log = calcular_porcentajes(error_log_values)
        porcentajes_inv = calcular_porcentajes(error_inv_values)
        porcentajes_binomial = calcular_porcentajes(error_binomial_values)
        porcentajes_arctan = calcular_porcentajes(error_arctan_values)

        # Crear el mensaje con los resultados
        resultados = (
            f"Porcentajes de Error Cos: >0.1: {porcentajes_cos[0]:.2f}%, <=0.1: {porcentajes_cos[1]:.2f}%\n"
            f"Porcentajes de Error Exp: >0.1: {porcentajes_exp[0]:.2f}%, <=0.1: {porcentajes_exp[1]:.2f}%\n"
            f"Porcentajes de Error Sen: >0.1: {porcentajes_sen[0]:.2f}%, <=0.1: {porcentajes_sen[1]:.2f}%\n"
            f"Porcentajes de Error Log: >0.1: {porcentajes_log[0]:.2f}%, <=0.1: {porcentajes_log[1]:.2f}%\n"
            f"Porcentajes de Error Inv: >0.1: {porcentajes_inv[0]:.2f}%, <=0.1: {porcentajes_inv[1]:.2f}%\n"
            f"Porcentajes de Error Binomial: >0.1: {porcentajes_binomial[0]:.2f}%, <=0.1: {porcentajes_binomial[1]:.2f}%\n"
            f"Porcentajes de Error Arctan: >0.1: {porcentajes_arctan[0]:.2f}%, <=0.1: {porcentajes_arctan[1]:.2f}%"
        )
        return resultados
    else:
        return f"El archivo '{nombre_archivo}' no existe."
# Función para crear un archivo CSV con datos que tengan error > 0.1
def crear_dataset_errores_mayor():
    nombre_archivo = nombre_archivo_var.get()
    nombre_archivo_salida = nombre_archivo_salida_var.get()
    if nombre_archivo and nombre_archivo_salida:
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'r', newline='') as archivo:
                reader = csv.DictReader(archivo)
                encabezado = reader.fieldnames
                
                # Filtrar filas con error > 0.1
                filas_filtradas = [
                    fila for fila in reader
                    if (float(fila['Error Cos']) > 0.1 or
                        float(fila['Error Exp']) > 0.1 or
                        float(fila['Error Sen']) > 0.1 or
                        float(fila['Error Log']) > 0.1 or
                        float(fila['Error Inv']) > 0.1 or
                        float(fila['Error Binomial']) > 0.1 or
                        float(fila['Error Arctan']) > 0.1)
                ]
            
            # Escribir las filas filtradas en un nuevo archivo CSV
            with open(nombre_archivo_salida, 'w', newline='') as archivo_salida:
                writer = csv.DictWriter(archivo_salida, fieldnames=encabezado)
                writer.writeheader()
                writer.writerows(filas_filtradas)
            
            messagebox.showinfo("Éxito", f"Archivo '{nombre_archivo_salida}' creado con datos filtrados.")
        else:
            messagebox.showerror("Error", f"El archivo '{nombre_archivo}' no existe.")
    else:
        messagebox.showerror("Error", "Debe seleccionar un archivo y proporcionar un nombre para el archivo de salida.")
# Interfaz gráfica
def seleccionar_archivo():
    archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    nombre_archivo_var.set(archivo)

def crear_archivo():
    archivo = nombre_archivo_var.get()
    if archivo:
        crear_archivo_csv(archivo)
    else:
        messagebox.showerror("Error", "Debe seleccionar un archivo.")

def agregar_datos():
    archivo = nombre_archivo_var.get()
    if archivo:
        agregar_datos_csv(archivo, cantn_var.get())
    else:
        messagebox.showerror("Error", "Debe seleccionar un archivo.")

def mostrar_datos():
    archivo = nombre_archivo_var.get()
    if archivo:
        mostrar_datos_csv(archivo)
    else:
        messagebox.showerror("Error", "Debe seleccionar un archivo.")

def graficar_datos():
    archivo = nombre_archivo_var.get()
    if archivo:
        graficar_csv(archivo)
    else:
        messagebox.showerror("Error", "Debe seleccionar un archivo.")
# Función para mostrar los porcentajes en un cuadro de mensaje
def mostrar_porcentajes():
    nombre_archivo = nombre_archivo_var.get()  # Reemplazar con el nombre real del archivo
    resultados = Porcentajes(nombre_archivo)
    messagebox.showinfo("Porcentajes de Errores", resultados)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de archivos CSV")
root.geometry("800x800")

# Variables de control
nombre_archivo_var = tk.StringVar()
nombre_archivo_salida_var = tk.StringVar()
cantn_var = tk.IntVar(value=3)

# Componentes de la interfaz
ttk.Label(root, text="Archivo CSV:").pack(pady=5)
ttk.Entry(root, textvariable=nombre_archivo_var, width=40).pack(pady=5)
ttk.Button(root, text="Seleccionar archivo", command=seleccionar_archivo).pack(pady=5)

ttk.Label(root, text="Nombre del archivo de salida:").pack(pady=5)
ttk.Entry(root, textvariable=nombre_archivo_salida_var, width=40).pack(pady=5)

ttk.Label(root, text="Seleccione el valor de N para Taylor:").pack(pady=5)
ttk.Radiobutton(root, text="N = 3", variable=cantn_var, value=3).pack(pady=5)
ttk.Radiobutton(root, text="N = 5", variable=cantn_var, value=5).pack(pady=5)
ttk.Radiobutton(root, text="N = 7", variable=cantn_var, value=7).pack(pady=5)
ttk.Radiobutton(root, text="N = 10", variable=cantn_var, value=10).pack(pady=5)
ttk.Radiobutton(root, text="N = 12", variable=cantn_var, value=12).pack(pady=5)
ttk.Radiobutton(root, text="N = 13", variable=cantn_var, value=13).pack(pady=5)

ttk.Button(root, text="Crear archivo CSV", command=crear_archivo).pack(pady=5)
ttk.Button(root, text="Agregar datos", command=agregar_datos).pack(pady=5)
ttk.Button(root, text="Mostrar datos", command=mostrar_datos).pack(pady=5)
ttk.Button(root, text="Graficar datos", command=graficar_datos).pack(pady=5)
# Crear y agregar el botón para mostrar los porcentajes de errores
boton_porcentajes = ttk.Button(root, text="Mostrar Porcentajes de Errores", command=mostrar_porcentajes)
boton_porcentajes.pack(pady=10)

# Botón para crear el dataset con errores > 0.1
ttk.Button(root, text="Crear Dataset con Errores > 0.1", command=crear_dataset_errores_mayor).pack(pady=10)
# Crear y agregar el botón para graficar los errores del CSV de salida
boton_graficar_errores = ttk.Button(root, text="Graficar Errores del CSV de Salida", command=lambda: graficar_csv_errores(nombre_archivo_salida_var.get()))
boton_graficar_errores.pack(pady=10)
# Ejecutar la interfaz
root.mainloop()
