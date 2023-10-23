facturas = {}

def mostrar_estado():
    total_cobrado = sum(facturas.values())
    total_pendiente = sum(facturas.values())
    print("Facturas pendientes de cobro:")
    for numero, costo in facturas.items():
        print(f"Factura #{numero}: ${costo}")
    print(f"Total cobrado: ${total_cobrado}")
    print(f"Total pendiente de cobro: ${total_pendiente}")

while True:
    print("\n¿Qué acción deseas realizar?")
    print("1 Añadir una nueva factura")
    print("2 Pagar una factura existente")
    print("3 Terminar")
    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == "1":
        numero = input("Introduce el número de factura: ")
        costo = float(input("Introduce el costo de la factura: "))
        facturas[numero] = costo
        mostrar_estado()

    elif opcion == "2":
        numero = input("Introduce el número de factura que deseas pagar: ")
        if numero in facturas:
            del facturas[numero]
            mostrar_estado()
        else:
            print(f"La factura #{numero} no existe en el diccionario.")

    elif opcion == "3":
        print("Programa terminado.")
        break

    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
