fecha_usuario=input('Ingresa fecha(dd/mm/aa): ')
split=fecha_usuario.split('/')

fecha={}
fecha['dia']=split[0]
fecha['mes']=split[1]
fecha['anio']=split[2]

mes={
    '01':'Enero',
    '02':'Febrero',
    '03':'Marzo',
    '04':'Abril',
    '05':'Mayo',
    '06':'Junio',
    '07':'Julio',
    '08':'Agosto',
    '09':'Septiembre',
    '10':'Octubre',
    '11':'Noviembre',
    '12':'Diciembre'
      }

print(fecha.get('dia'), 'de', mes.get(fecha.get('mes')), 'de', fecha.get('anio'))