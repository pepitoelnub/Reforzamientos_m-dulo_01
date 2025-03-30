"""Realizar un programa donde se ingresarán por consola los nombres de los
alumnos (indicar previamente la cantidad de alumnos a ingresar) de un curso
y las notas de c/u. Guardarás la información en un diccionario donde las claves
serán los nombres de c/u de estos alumnos y sus valores serán las notas de
esto alumnos.
Finalmente mostrarás los alumnos con sus notas en un mensaje similar a
“Pedro tiene la nota de 15” y también la media de todas las notas."""
# cantidad de alumnos
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

# Crear diccionario para almacenar nombres y notas
notas_alumnos = {}

# nombres y notas de los alumnos
for _ in range(cantidad_alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    notas_alumnos[nombre] = nota

# alumnos con sus notas
for nombre, nota in notas_alumnos.items():
    print(f"{nombre} tiene la nota de {nota}")

# media de las notas
media_notas = sum(notas_alumnos.values()) / cantidad_alumnos
print(f"La media de todas las notas es: {media_notas:.2f}")