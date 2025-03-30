"""Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los
datos mediante consola también (5 compañías relacionadas con al mundo de
TI) y harás una copia donde adrede agregarás nombres que estarán
repetidos (mediante consola) para que finalmente muestres otra lista donde
solo se mostrará los nombres no repetidos y también la lista inicial"""
#Tamaño de lista
lista = []
n = int(input("Ingresa el tamaño de la lista: "))
print("A continuación ingresa conpañias relacionadas al mundo de TI")
for i in range(n):
    compañias = input(f"Compañia {i+1}: ")
    lista.append(compañias)
#Copia
lista_02 = lista.copy()
print("A continuación ingrese compañias repetidas:")
compañias_01 = input("Compañia 1: ")
compañias_02 = input("Compañia 2: ")
lista_02.append(compañias_02)
lista_02.append(compañias_01)
lista_03 = lista_02.copy()
lista_03.remove(compañias_02)
lista_03.remove(compañias_02)
lista_03.remove(compañias_01)
lista_03.remove(compañias_01)
print(lista_03)

print(lista)
