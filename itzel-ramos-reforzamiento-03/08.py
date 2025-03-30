"""
Escribir un programa donde ingresará 8 nombres de países. Se quiere
hacer un clon de la lista, esta copia se le eliminará el primer y penúltimo
valor, mostrar finalmente el tamaño de la lista modificada, la lista original
y todos sus elementos de la lista modificada.
"""
paises = []
for i in range(8):
    pais = input(f"Ingrese el nombre de 8 países {i+1}: ")
    paises.append(pais)
Copia = paises.copy()

del Copia[0]
del Copia[-2]

print("\nLista original de países:", paises)
print("Lista modificada de países:", Copia)
print("Tamaño de la lista modificada:", len(Copia))