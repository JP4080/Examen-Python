# Variables Numericas y Operaciones Basicas.
a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b
modulo = a % b
potencia = a ** b

print("Suma:", suma)                        # Responde: 13
print("Resta:", resta)                      # Responde: 7
print("Multiplicación:", multiplicacion)    # Responde: 30
print("División:", division)                # Responde: 3.333...
print("División entera:", division_entera)  # Responde: 3
print("Módulo:", modulo)                    # Responde: 1
print("Potencia:", potencia)                # Responde: 1000



# Operaciones de Comparación 
x = 5
y = 8

igual = x == y
diferente = x != y
mayor = x > y
menor = x < y
mayor_igual = x >= y
menor_igual = x <= y

print("¿x == y?", igual)            # Resulta: False
print("¿x != y?", diferente)        # Resulta: True
print("¿x > y?", mayor)             # Resulta: False
print("¿x < y?", menor)             # Resulta: True
print("¿x >= y?", mayor_igual)      # Resulta: False
print("¿x <= y?", menor_igual)      # Resulta: True



# Operaciones Lógicas
cond1 = True
cond2 = False

and_logico = cond1 and cond2
or_logico = cond1 or cond2
not_logico = not cond1

print("AND lógico:", and_logico)    # Arroja: False
print("OR lógico:", or_logico)      # Arroja: True
print("NOT lógico:", not_logico)    # Arroja: False



# Funciones Strings
texto = "Hola Python"

mayusculas = texto.upper()
minusculas = texto.lower()
longitud = len(texto)
reemplazo = texto.replace("Python", "Mundo")

print("Mayúsculas:", mayusculas)       # Imprime: "HOLA, PYTHON"
print("Minúsculas:", minusculas)       # Imprime: "hola, python"
print("Longitud del texto:", longitud) # Imprime: 12
print("Texto reemplazado:", reemplazo) # Imprime:"Hola, Mundo"



# Funciones Listas
lista = [1, 2, 3]               
lista.append(4)                 
lista.remove(2)                 
longitud_lista = len(lista)     
lista.sort()                    

print("Lista actualizada:", lista)           # Presenta: [1, 3, 4]
print("Longitud de lista:", longitud_lista)  # Presenta: 3



# Funciones Diccionarios
diccionario = {"nombre": "Ana", "edad": 25} 
claves = diccionario.keys()                
valores = diccionario.values()             
diccionario["ciudad"] = "Bogotá"            
del diccionario["edad"]                    

print("Claves del diccionario:", claves)       # Responde: ['nombre', 'ciudad']
print("Valores del diccionario:", valores)     # Responde: ['Ana', 'Bogotá']
print("Diccionario final:", diccionario)       # Responde: {'nombre': 'Ana', 'ciudad': 'Bogotá'}



# Conversión de Tipos
numero = 10
texto_numero = str(numero)
lista_texto = list("Hola")
numero_flotante = float("3.14")

print("Número convertido a texto:", texto_numero)               # Genera: "10"
print("Texto convertido a lista:", lista_texto)                 # Genera: ['H', 'o', 'l', 'a']
print("Texto convertido a número flotante:", numero_flotante)   # Genera: 3.14