"""4. Crear un diccionario con 6 departamentos en el país.
- Borrar cualquier departamento, usando la palabra reservada del.
- Actualizar el penúltimo departamento por otro.
- Comprobar que no existe este departamento borrado dentro del
diccionario."""
#Creo
Diccionario = { "Lima": "Costa", "Cusco": "Sierra", "Arequipa": "Sierra", "Loreto": "Selva", "Piura": "Costa", "Puno": "Sierra"}
print(Diccionario)
#Elimino
del Diccionario["Cusco"]
#Remplazo
Diccionario["Piura"] = "Lambayeque"
#Compruebo
print(Diccionario)