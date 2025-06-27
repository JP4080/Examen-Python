#--------------------------Crear Una Ventana-------------------------------

import tkinter as tk #Para importar la libreria y abreviarla

ventana = tk.Tk() #Ejecuta un contenedor y se guarda como variable "ventana"
ventana.title("Ventana De Prueba") #Da el titulo al contenedor
ventana.geometry("500x350") #Define el tamaño de la ventana (Width x Height)

etiqueta = tk.Label(ventana, text="Texto De Prueba", font=("Arial", id)) #Crea una tabla como "etiqueta", luego se definen sus caracteristicas
etiqueta.pack(pady=50, padx=50, expand=True) #Muestra automaticamente el elemento de forma organizada

ventana.mainloop() #Bucle para iniciar la interfaz gráfica


#----------------------------Crear Un Boton---------------------------------

import tkinter as tk #Para importar la libreria y abreviarla

def cambiar_texto(): #Se define una funcion
    etiqueta.config(text="Cambio De Texto") #Utiliza el metodo para modificar la propiedad

ventana = tk.Tk() #Ejecuta un contenedor y se guarda como variable "ventana"
ventana.title("Botón interactivo") #Da el titulo al contenedor
ventana.geometry("500x350") #Define el tamaño de la ventana (Width x Height)

etiqueta = tk.Label(ventana, text="Texto original", font=("Arial", 14)) #Crea una etiqueta, luego se definen sus caracteristicas
etiqueta.pack(pady=10) #Muestra automaticamente el elemento de forma organizada

boton = tk.Button(ventana, text="Cambiar texto", command=cambiar_texto) #Crea el boton, junto sus caracteristicas
boton.pack(pady=10) #Muestra automaticamente el elemento de forma organizada

ventana.mainloop() #Bucle para iniciar la interfaz gráfica


#------------------------Cambiar Fondo De La Ventana-----------------------------

import tkinter as tk  #Para importar la librería y abreviarla

def fondo_rojo():  #Se define una función que se ejecutará al presionar el botón rojo
    ventana.config(bg="red")  #Cambia el color de fondo de la ventana

def fondo_verde():  #Se define una función que se ejecutará al presionar el botón verde
    ventana.config(bg="green")  #Cambia el color de fondo de la ventana

def fondo_azul():  #Se define una función que se ejecutará al presionar el botón azul
    ventana.config(bg="blue")  #Cambia el color de fondo de la ventana

ventana = tk.Tk()  #Ejecuta un contenedor y se guarda como variable "ventana"
ventana.title("Cambiar color de fondo")  #Da el título al contenedor
ventana.geometry("300x200")  #Define el tamaño de la ventana (Width x Height)
ventana.config(bg="white")  #Establece el color inicial del fondo como blanco

boton_rojo = tk.Button(ventana, text="Rojo", command=fondo_rojo, bg="red", fg="white", font=("Arial", 12))  #Crea el botón rojo con sus propiedades
boton_rojo.pack(fill=tk.X, padx=20, pady=5)  #Muestra el botón y lo posiciona horizontalmente, con espacio alrededor

boton_verde = tk.Button(ventana, text="Verde", command=fondo_verde, bg="green", fg="white", font=("Arial", 12))  #Crea el botón verde con sus propiedades
boton_verde.pack(fill=tk.X, padx=20, pady=5)  #Muestra el botón verde con separación

boton_azul = tk.Button(ventana, text="Azul", command=fondo_azul, bg="blue", fg="white", font=("Arial", 12))  #Crea el botón azul con sus propiedades
boton_azul.pack(fill=tk.X, padx=20, pady=5)  #Muestra el botón azul con espacio a los lados y verticalmente

ventana.mainloop()  #Bucle para iniciar la interfaz gráfica


