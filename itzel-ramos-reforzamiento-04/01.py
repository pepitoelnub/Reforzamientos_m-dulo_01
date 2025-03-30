""""Escribir un programa donde ingresarás el tamaño de la lista mediante
consola, este tamaño servirá para ingresar una cantidad X de nombres de
alumnos. Ingresarás los nombres mediante consola también.
Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de
la lista que fueron ingresados."""
#El usuario ingresa en número de la lista
n = int(input("¿Cuánto alumnos hay? "))
#Creamos la lista
lista = []
for i in range(n):
    nombre = input(f"Ingrese nombre del alumno {i+1}: ")
    lista.append(nombre)

#Mostrar resultados
print("El tamaño de la lista es: ", len(lista))
print("Los nombres de los estudiantes son: ", lista)
