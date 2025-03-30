""""
Crea una siguiente lista vacía y agregue ítems a partir de variables (los cuales
tendrán los siguientes tipos de datos: 3 floats, 3 ints y 3 strings) (append).
Sumar las dos listas creadas anteriormente y mostrar el resultado en consola.
"""
#Creo lista vacía
lista_02 = []
#Creo variables
float_01 = 4.5
float_02 = 4.1
float_03 = 4.2
int_01 = 1
int_02 = 2
int_03 = 3
str_01 = "Hola"
str_02 = "Buenas"
str_03 = "Bienvenido"
#Agrego ítems
lista_02.append(float_01)
lista_02.append(float_02)
lista_02.append(float_03)
lista_02.append(int_01)
lista_02.append(int_02)
lista_02.append(int_03)
lista_02.append(str_01)
lista_02.append(str_02)
lista_02.append(str_03)
print("Mi lista vacía con las variables agregadas es: ", lista_02)
#Suma de listas creadas anteriormente, ejercicio 02 y 01
cursos_pregrado = ["bioquímica", "zoología", "botánica", "bioquímica", "biomatemática"]
lista_01 = ["Atún", "azúcar"]
suma_de_listas = cursos_pregrado + lista_01
print("Suma de listas de los ejercicios anteriores: ", suma_de_listas)
