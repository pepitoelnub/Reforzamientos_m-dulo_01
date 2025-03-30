"""
Crear un programa en Python donde tendrás una lista con 5
departamentos, ingresarás 2 departamentos adicionales por posición, el
cual el segundo departamento estará en la posición ‘1’ y el primero en
penúltimo lugar, finalmente mostrar la lista original y la lista actualizada
en terminal
"""
# Lista con 5 departamentos
departamentos = ["Ica", "Lima", "Arequipa", "Ayacucho", "Cuzco"]

# Mostrar la lista original
print("Lista original de departamentos:", departamentos)

# Ingresar 2 departamentos adicionales
departamento_1 = input("Ingrese el primer departamento (irá en la penúltima posición): ")
departamento_2 = input("Ingrese el segundo departamento (irá en la posición 1): ")

departamentos.insert(1, departamento_2)
departamentos.insert(-1, departamento_1)

# Mostrar la lista actualizada
print("\nLista actualizada de departamentos:", departamentos)