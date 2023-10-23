clientes = {}

def agregar_cliente():
    nif = input("Introduce el NIF del cliente: ")
    nombre = input("Introduce el nombre del cliente: ")
    direccion = input("Introduce la dirección del cliente: ")
    telefono = input("Introduce el teléfono del cliente: ")
    correo = input("Introduce el correo del cliente: ")
    preferente = input("¿Es un cliente preferente? (Sí/No): ").lower() == "sí"
    cliente = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "correo": correo,
        "preferente": preferente
    }
    clientes[nif] = cliente

def eliminar_cliente():
    nif = input("Introduce el NIF del cliente que deseas eliminar: ")
    if nif in clientes:
        del clientes[nif]
        print(f"Cliente con NIF {nif} eliminado de la base de datos.")
    else:
        print(f"El cliente con NIF {nif} no existe en la base de datos.")

def mostrar_cliente():
    nif = input("Introduce el NIF del cliente que deseas mostrar: ")
    if nif in clientes:
        cliente = clientes[nif]
        print(f"Datos del cliente con NIF {nif}:")
        for clave, valor in cliente.items():
            print(f"{clave.capitalize()}: {valor}")
    else:
        print(f"El cliente con NIF {nif} no existe en la base de datos.")

def listar_clientes():
    print("Lista de todos los clientes:")
    for nif, cliente in clientes.items():
        print(f"NIF: {nif}, Nombre: {cliente['nombre']}")

def listar_clientes_preferentes():
    print("Lista de clientes preferentes:")
    for nif, cliente in clientes.items():
        if cliente['preferente']:
            print(f"NIF: {nif}, Nombre: {cliente['nombre']}")

while True:
    print("\n¿Qué acción deseas realizar?")
    print("1 Añadir cliente")
    print("2 Eliminar cliente")
    print("3 Mostrar cliente")
    print("4 Listar todos los clientes")
    print("5 Listar clientes preferentes")
    print("6 Terminar")
    opcion = input("Selecciona una opción (1/2/3/4/5/6): ")

    if opcion == "1":
        agregar_cliente()

    elif opcion == "2":
        eliminar_cliente()

    elif opcion == "3":
        mostrar_cliente()

    elif opcion == "4":
        listar_clientes()

    elif opcion == "5":
        listar_clientes_preferentes()

    elif opcion == "6":
        print("Programa terminado.")
        break

    else:
        print("Opción no válida. Por favor, selecciona 1, 2, 3, 4, 5 o 6.")
