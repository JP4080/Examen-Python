Investigación de Librería de Python

# Libreria Investigada
Tkinter


# ¿Que Es?
tkinter es una librería que permite crear interfaces gráficas (ventanas) en Python. 


# ¿Su Funcionalidad?
Sirve para hacer programas con ventanas, botones, cuadros de texto, etiquetas, entre otros objetos o elementos visuales.
Es una herramienta básica para crear programas interactivos y con ventanas.


# Codificación Básica
Primero se importa la librería tkinter.
Luego se crea una ventana con Tk().
Después se agregan los elementos como etiquetas o botones.
Por último, se usa mainloop() para mantener la ventana abierta.


# Sintaxis Para Interfaz
import tkinter as tk

ventana = tk.Tk()
ventana.title("")
ventana.mainloop()


# Aplicaciones:
- Formularios sencillos con cuadros de texto.
- Calculadoras simples con botones.
- Interfaces visuales para programas escritos en Python.


# ¿Por Que Es Util?
- Permite crear programas con ventanas fácilmente.
- Ideal para principiantes que quieren aprender interfaces gráficas.
- No necesita instalación adicional → viene incluido con Python.


# Ejemplo De Codificacion
import tkinter as tk

# Crear Ventana
ventana = tk.Tk()                       # Crea la ventana
ventana.title("Ventana con tkinter")    # Su respectivo titulo
ventana.geometry("300x150")             # Tamaño de la ventana (ancho x alto)

# Crear Etiqueta o Texto
etiqueta = tk.Label(ventana, text="Esta es una interfaz")    # Crea un texto
etiqueta.pack()                                              # Muestra el texto

# Crear Botón para Imprimir un Mensaje en Consola
def saludar():
    print("¡Hola desde el botón!")           # Funcion para el boton

boton = tk.Button(ventana, text="Saludar", command=saludar)     # Crea un boton
boton.pack()                                                    # Muestra el boton

ventana.mainloop()        # Mantiene la ventana hasta que el usuario la cierre