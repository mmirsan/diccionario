mi_diccionario =  {'Euro':'€', 'Dollar':'$', 
'Yen':'Y'}

divisa = input("INTRODUCE UNA DIVISA ")
print(f'{divisa} = {mi_diccionario.get(divisa, "No es valida")}')

