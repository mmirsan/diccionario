nombre = input("Cual es tu nombre ")
edad = input("Cual es tu edad ")
direccion = input("Cual es tu direccion ")
telefono = input("cual es tu numero de telefono ")

persona = {}
persona["nombre"] = nombre

persona["edad"] = edad

persona["direccion"] = direccion

persona["telefono"] = telefono

print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])