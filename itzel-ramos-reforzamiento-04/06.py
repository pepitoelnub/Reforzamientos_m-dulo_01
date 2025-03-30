"""Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario
actualizado."""
Diccionario = { "nombre": "Itzel", "Edad": 17, "Salario": 1000, "Edad": 17}
Diccionario["DNI"] = 61087032
DNI = Diccionario["DNI"]
Salario = Diccionario["Salario"]
print(DNI)
print(Salario)
del Diccionario["Edad"]
print("El diccionario actualizado es: ", Diccionario)


