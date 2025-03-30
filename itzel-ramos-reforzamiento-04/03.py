"""Tienes una lista con 5 nombres de estudiantes. Crear un programa que te
pedirá ingresar el nombre de un estudiante, la cuál será eliminada de lista
inicial en caso que no exista en la lista mostrar un mensaje donde indique
que no se encuentre en la lista y esta será agregada a la lista.
 Finalmente mostrar la lista actualizada en consola."""
#Creo la lista
estudiantes = ["Itzel", "Antony", "Roberto", "Abner", "José"]
print(estudiantes)
#Usuario responde
nombre = input("Ingrese el nombre del estudiante que desea eliminar: ")
if nombre in estudiantes:
    estudiantes.remove(nombre)
    print("La lista actualizada es: ", estudiantes)
else:
    estudiantes.append(nombre)
    print("No se encontró al estudiante. Será agregado a la lista.")
    print("Lista actualizada: ", estudiantes)

