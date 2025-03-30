"""Crear un programa en Python donde tendrás una lista con 5 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo
departamento que ingreses sustituirá al primero de la lista."""
#Creo la lista
departamentos = ["Ica", "Ayacucho", "Madre de Dios", "Cuzco", "Puno"]
#Respuesta del usuario
nuevo_depa_01 = input("Ingrese el nombre del primer departamento: ")
departamentos.append(nuevo_depa_01)
nuevo_depa_02 = input("Ingrese el nombre del segundo departamento: ")
departamentos[0] = nuevo_depa_02
print(departamentos)

