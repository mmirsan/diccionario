articulo1 = input("INTRODUCE EL ARTICULO1")
precio1 = int(input("INTRODUCE EL PRECIO ARTICULO1"))
articulo2 =input("INTRODUCE EL ARTICULO2 ")
precio2 = int(input("INTRODUCE EL precio2"))
articulo3 = input("INTRODUCE EL ARTICULO3 ")
precio3 = int(input("INTRODUCE EL PRECIO3"))


cesta_compra = {}
cesta_compra[articulo1] = precio1
cesta_compra[articulo2] = precio2
cesta_compra[articulo3] = precio3


print(cesta_compra)
print("El total es ", precio1+precio2+precio3)