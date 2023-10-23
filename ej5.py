asignaturas_creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos_curso = 0

for asignatura, creditos in asignaturas_creditos.items():
    print(f'{asignatura} tiene {creditos} créditos')
    total_creditos_curso += creditos

print(f'El número total de créditos del curso es: {total_creditos_curso}')
