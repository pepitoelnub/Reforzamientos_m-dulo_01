"""
Agregar 5 Objetos nuevos a tu lista (append) y quitar 2 elementos de esta
lista por valor. Mostrar la lista final en la terminal.
Obtén también la cantidad total ítems que tienes en tu lista ya creada para
agregar este valor a tu lista y mostrar también el resultado final de cantidad
total de elemento y la lista actualizada en consola.
"""
# Creo mi lista
lista_01 = ["Atún", "azúcar"]
# Agrego 5 objetos a mi lista usando append
lista_01.append("arroz")
lista_01.append("cebolla")
lista_01.append("ajo")
lista_01.append("sal")
lista_01.append("tomate")
# Quito dos elementos de esta lista por valor
lista_01.remove("Atún")
lista_01.remove("azúcar")
print(lista_01)
# Obtengo la cantidad de items
print(len(lista_01))
# Agrego la cantidad de item a la lista
lista_01.append(5)
# Muestro la cantidad final de items y la lista actualizada
print(len(lista_01))
print(lista_01)
