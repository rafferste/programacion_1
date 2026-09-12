notas = [3, 6, 8, 3, 5, 1, 7, 9, 10, 7]
promedio = 0
suma = 0
nota_mas_alta = 0
nota_mas_baja = 10

for i in range(len(notas)):
    print(notas[i])
    nota = notas[i]
    suma += nota

    if nota < nota_mas_baja:
        nota_mas_baja = nota
    elif nota > nota_mas_alta:
        nota_mas_alta = nota

promedio = suma / len(notas)
print(f"Promedio: {promedio}")
print(f"Nota mas alta: {nota_mas_alta}")
print(f"Nota mas baja: {nota_mas_baja}")
