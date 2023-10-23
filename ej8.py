def crear_diccionario_traduccion():
    datos = input("Introduce las palabras en español e inglés separadas por dos puntos y separa los pares por comas: ")
    return dict(par.strip().split(':') for par in datos.split(','))

def traducir_frase(frase, diccionario):
    return ' '.join(diccionario.get(palabra, palabra) for palabra in frase.split())

diccionario_traduccion = crear_diccionario_traduccion()

frase_en_espanol = input("Introduce una frase en español: ")

frase_traducida = traducir_frase(frase_en_espanol, diccionario_traduccion)

print("Frase traducida:", frase_traducida)
