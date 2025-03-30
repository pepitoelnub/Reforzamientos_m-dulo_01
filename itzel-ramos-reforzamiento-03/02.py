"""
Devuelve la cantidad de veces que se repite un curso que hayas llevado en
pregrado (agregarlos previamente a la lista con un mínimo de 5 cursos) luego
mostrarla, finalmente elimina el segundo ítem de la lista usando debidamente
su índice y mostrar en consola tu lista actualizada
"""
#Lista de cursos
cursos_pregrado = ["bioquímica", "zoología", "botánica", "bioquímica", "biomatemática"]
#Cantidad de veces que se repite un curso
print("Bioquímica se repite {} veces.".format(cursos_pregrado.count("bioquímica")))
#elimino el segundo item de la lista usando su indice
del cursos_pregrado[1]
#muestro la lista actualizada
print("La lista actualizada es: ", cursos_pregrado)
