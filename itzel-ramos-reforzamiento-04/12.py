"""Crear una agenda basada en un diccionario donde los key serán los nombres
de las personas y sus “values” serán los números de teléfono de c/u.
Ingresarás por consola el nombre y el número de cada persona que serán
registrados en la agenda.
El programa también te permitirá buscar por nombre en el diccionario en caso
no exista mostrar un mensaje de “No se encuentra registrado en la agenda”
"""
agenda = {}

total_contactos = int(input("Ingrese la cantidad de contactos a registrar: "))
#ingreso de contanctos
for _ in range(total_contactos):
    nombre = input("Ingrese el nombre de la persona: ")
    telefono = input(f"Ingrese el número de teléfono de {nombre}: ")
    agenda[nombre] = telefono

# Búsqueda
nombre_buscar = input("Ingrese el nombre a buscar en la agenda: ")
if nombre_buscar in agenda:
    print(f"{nombre_buscar} está registrado con el número {agenda[nombre_buscar]}")
else:
    print("No se encuentra registrado en la agenda")