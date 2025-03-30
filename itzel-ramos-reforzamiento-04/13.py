""""Una empresa desea gestionar las facturas pendientes que tiene por pagar,
para esto se creará un diccionario donde tendrá por key el número de factura
“00054” y su value será el coste de la factura. El programa tendrá la opción
de pedir nueva factura (por consola) que se agregará al diccionario. Cada vez
que el área de contabilidad pague una factura se pedirá el número de factura
que fue cancelada, si existe mostrar un mensaje donde indicará “La factura
ya está cancelada” caso contrario “El número de factura no existe”
Considerar que cada vez que se realice algún pago o ingreso de una nueva
factura se mostrará inmediatamente al diccionario actualizado.
"""
# Crear diccionario
facturas = {"00054": 100}  # Factura inicial

while True:
    print("\nOpciones:")
    print("1. Agregar nueva factura")
    print("2. Pagar factura")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        numero_factura = input("Ingrese el número de factura: ")
        costo = float(input("Ingrese el coste de la factura: "))
        facturas[numero_factura] = costo
        print("Factura agregada con éxito.")

    elif opcion == "2":
        numero_factura = input("Ingrese el número de factura a pagar: ")
        if numero_factura in facturas:
            del facturas[numero_factura]
            print("La factura ya está cancelada.")
        else:
            print("El número de factura no existe.")

    elif opcion == "3":
        break

    else:
        print("Opción no válida, intente nuevamente.")

    print("\nFacturas pendientes:")
    print(facturas)
