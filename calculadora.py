import tkinter as tk

# Funciones para realizar operaciones matemáticas
def sumar():
    resultado.set(float(entrada1.get()) + float(entrada2.get()))

def restar():
    resultado.set(float(entrada1.get()) - float(entrada2.get()))

def multiplicar():
    resultado.set(float(entrada1.get()) * float(entrada2.get()))

def dividir():
    try:
        resultado.set(float(entrada1.get()) / float(entrada2.get()))
    except ZeroDivisionError:
        resultado.set("Error: división por cero")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.configure(bg="#E5E5E5")  # Color de fondo

# Estilos
entry_style = {"fg": "#333333", "font": ("Arial", 12)}
button_style = {"bg": "#4CAF50", "fg": "white", "font": ("Arial", 12, "bold")}

# Contenedor principal
container = tk.Frame(ventana, bg="#E5E5E5")
container.pack(padx=10, pady=10)

# Etiquetas y campos de entrada para números y resultado
tk.Label(container, text="Número 1:", bg="#E5E5E5", **entry_style).grid(row=0, column=0, padx=5, pady=5)
entrada1 = tk.Entry(container, **entry_style)
entrada1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(container, text="Número 2:", bg="#E5E5E5", **entry_style).grid(row=1, column=0, padx=5, pady=5)
entrada2 = tk.Entry(container, **entry_style)
entrada2.grid(row=1, column=1, padx=5, pady=5)

resultado = tk.StringVar()
resultado.set("Resultado")
resultado_label = tk.Label(container, textvariable=resultado, bg="#E5E5E5", fg="#333333", font=("Arial", 12, "bold"))
resultado_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Botones para operaciones
boton_suma = tk.Button(container, text="+", command=sumar, **button_style)
boton_suma.grid(row=3, column=0, padx=5, pady=5)

boton_resta = tk.Button(container, text="-", command=restar, **button_style)
boton_resta.grid(row=3, column=1, padx=5, pady=5)

boton_multiplicacion = tk.Button(container, text="*", command=multiplicar, **button_style)
boton_multiplicacion.grid(row=4, column=0, padx=5, pady=5)

boton_division = tk.Button(container, text="/", command=dividir, **button_style)
boton_division.grid(row=4, column=1, padx=5, pady=5)

# Mostrar la ventana
ventana.mainloop()

# Realizado por Brian Andres Serna