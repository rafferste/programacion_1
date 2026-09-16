notas = matriz_notas = [
    [8.5, 9.0, 7.5],
    [7.0, 8.0, 8.5],
    [9.5, 10.0, 9.0],
    [6.0, 7.5, 6.5],
    [8.0, 8.5, 9.0]
]
materia1 = 0
materia2 = 0
materia3 = 0
contador = 1

for estudiante in notas:
    suma_estudiante = 0
    materia1 += estudiante[0]
    materia2 += estudiante[1]
    materia3 += estudiante[2]

    for nota in estudiante:
        suma_estudiante += nota

    promedio_estudiante = suma_estudiante / 3   
    print(f"Estudiante {contador}: {promedio_estudiante}")
    print(f"Materia 1: {materia1}")
    print(f"Materia2: {materia2}")
    print(f"Materia3: {materia3}")
    