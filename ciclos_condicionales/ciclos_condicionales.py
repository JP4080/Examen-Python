# Bucle for
for i in range(5):
    print("Número en for:", i)
# Imprime números del 0 al 4



# Bucle while 
contador = 0

while contador < 5:
    contador += 1

    if contador == 3:
        continue        # Salta el 3

    if contador == 5:
        break           # Detiene el ciclo

    print("Contador en while:", contador)
# Ejecuta mientras contador sea menor a 5



# Bucle else
for letra in "Hola":
    print(letra)
else:
    print("For terminado")
# Se ejecuta si el for termina sin break



# Condicionales
edad = 20

if edad < 18:
    print("Menor de edad")
elif edad >= 18 and edad < 65:
    print("Adulto")
else:
    print("Adulto mayor")
# Muestra según la edad