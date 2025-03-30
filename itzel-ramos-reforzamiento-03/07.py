""""
Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
finalmente muestra la suma y la media de los números ingresado insertados en
la terminal
"""
#Creo lista vacía
Lista_03 = []
#Ingreso los valores
Lista_03.extend([4.3, 5, 10, 9, 30, 40,2, 8, 9, 10])
#Suma
suma = sum(Lista_03)
print("La suma de los elementos de mi lista es: ", suma)
#Media
media = sum(Lista_03) / len(Lista_03)
print("La media de los elementos de mi lista es: ", media)
