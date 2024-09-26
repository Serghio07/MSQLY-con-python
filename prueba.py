import tkinter as tk

# Crear ventana simple
ventana = tk.Tk()
ventana.title("Prueba Tkinter")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="¡Tkinter está funcionando!")
etiqueta.pack(pady=20)

# Iniciar el bucle de la ventana
ventana.mainloop()
