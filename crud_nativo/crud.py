# Lista
productos = []



# Crear producto
def crear(nombre):
    productos.append(nombre)
    print("Producto agregado:", nombre)



# Leer producto
def leer():
    print("Lista de productos:", productos)



# Actualizar producto
def actualizar(posicion, nuevo_nombre):
    if 0 <= posicion < len(productos):
        productos[posicion] = nuevo_nombre
        print("Producto actualizado:", nuevo_nombre)
    else:
        print("Posición no válida")



# Eliminar producto 
def eliminar(posicion):
    if 0 <= posicion < len(productos):
        productos[posicion] = "Eliminado"
        print("Producto eliminado en posición:", posicion)
    else:
        print("Posición no válida")



# Ejemplo
leer()                   # Mostrar productos (vacio)
crear("Papel")           # Agregar "Papel"
crear("Cuaderno")        # Agregar "Cuaderno"
leer()                   # Mostrar productos (reciente)
actualizar(0, "Carton")  # Cambiar "Papel" por "Carton"
leer()                   # Mostrar productos (actualizado)
eliminar(1)              # Eliminar "Cuaderno"
leer()                   # Mostrar productos (finales)
