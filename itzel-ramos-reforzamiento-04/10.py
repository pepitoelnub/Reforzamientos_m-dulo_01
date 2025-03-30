"""Ingresar por consola 4 números mediante consola, crear un diccionario
donde los ‘key’ serán los números indicados y los valores serán los cubos de
las estos keys. Mostrar finalmente este diccionario."""
numeros = [int(input(f"Ingresa el número que desees: ")) for i in range(4)]
dicc = {num: num**3 for num in numeros}
print(dicc) 