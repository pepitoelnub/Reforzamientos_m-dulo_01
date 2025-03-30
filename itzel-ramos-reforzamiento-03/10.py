"""
Tienes una lista con 7 diferentes nombres de BD relacionales. De la cual 3
BDs estarán repetidas adrede (en posiciones no consecutivas), sacar la
base de datos repetidas uno por valor y le otro por índice.
Finalmente mostrar la lista actualizada en consola
"""
# Lista con 7 bases de datos relacionales
bd_relacionales = ["MySQL", "PostgreSQL", "Oracle", "SQL Server", "MySQL", "SQLite", "Oracle"]

# Eliminar una base de datos repetida por valor
bd_relacionales.remove("MySQL")

# Eliminar otra base de datos repetida por índice
indice = bd_relacionales.index("Oracle")
del bd_relacionales[indice]

# Mostrar la lista actualizada
print("Lista actualizada de bases de datos:", bd_relacionales)