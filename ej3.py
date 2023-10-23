fruta={'platano':135, 'manzana':80, 'pera':85,'naranja':70}

ingreso=input('Por favor ingrese una fruta: ')
kilos=float (input('Por favor ingrese los kilos que desea: '))

if fruta.get(ingreso) is None:
    print('La fruta ingresada no se encuentra en el sistema.')
else:
    print('El precio total es $', fruta.get(ingreso)*kilos)