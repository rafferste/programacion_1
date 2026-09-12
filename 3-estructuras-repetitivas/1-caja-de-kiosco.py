nombre = ""
cantidad = ""
total_sin_descuento = 0
total_con_descuento = 0
promedio = 0
ahorro = 0

while not nombre.isalpha():
    nombre = input("Cliente: ")


while not cantidad.isdigit():
    cantidad = input("Cantidad de productos: ")
cantidad = int(cantidad)

for producto in range(cantidad):
    precio = ""
    descuento = ""

    while not precio.isdigit():
        precio = input(f"Producto {producto+1} - Precio: ")
    precio = int(precio)

    while descuento != "S" and descuento != "N":
        descuento = input("Descuento (S/N): ")
        descuento = descuento.upper()

    total_sin_descuento += precio
    if descuento == "S":
        precio = precio * 0.9
    total_con_descuento += precio

promedio = total_con_descuento / cantidad
ahorro = total_sin_descuento - total_con_descuento

print(f'''
Total sin descuentos: ${total_sin_descuento}
Total con descuentos: ${total_con_descuento}
Ahorro: ${ahorro}
Promedio por producto: ${promedio}
''')