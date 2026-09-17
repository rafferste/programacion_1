ventas = [
    [15, 20, 12, 45, 30, 25, 50],  # Producto 1
    [10, 18, 32, 14, 22, 12, 15],  # Producto 2
    [40, 55, 60, 30, 45, 50, 66],  # Producto 3
    [22, 15, 18, 20, 25, 30, 28]   # Producto 4
]
suma_ventas_dias = [0, 0, 0, 0, 0, 0, 0]
dia_mayor_ventas = 0
prodcuto_mayor_ventas = [0, 0]
cant_productos = len(ventas)

print("Ventas totales")
for i in range(cant_productos):
    ventas_totales = sum(ventas[i])
    print(f"Producto {i + 1}: {ventas_totales}")
    if ventas_totales > prodcuto_mayor_ventas[1]:
        prodcuto_mayor_ventas = [i+1, ventas_totales]

    for j in range(7):
        suma_ventas_dias[j] += ventas[i][j]

cont = 0
for dia in suma_ventas_dias:
    if dia > dia_mayor_ventas:
        dia_mayor_ventas = dia
    cont += 1

print(f"Dia mayor ventas: {cont}")
print(f"Ventas: {dia_mayor_ventas}")
print(f"Producto mas vendido: {prodcuto_mayor_ventas[0]}")
print(f"Ventas: {prodcuto_mayor_ventas[1]}")