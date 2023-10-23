persona = {}

while True:
    dato = input("Ingrese el nombre del dato (o escriba 'salir' para finalizar): ")

    if dato.lower() == 'salir':
        break

    valor = input(f"Ingrese el valor para {dato}: ")
    persona[dato] = valor

print("Información de la persona:")
for key, value in persona.items():
    print(f"{key}: {value}")
