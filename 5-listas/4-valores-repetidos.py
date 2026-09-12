datos = [1, 2, 5, 3, 7, 1, 9, 5, 3]
print(datos)
datos_sin_repetir = list()

for i in range(len(datos)):
    numero = datos[i]
    if not numero in datos_sin_repetir:
        datos_sin_repetir.append(numero)

print(datos_sin_repetir)