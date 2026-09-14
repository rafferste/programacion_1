numeros = [1, 2, 3, 4, 5, 6, 7]
print(f"Lista de numeros: {numeros}")
tamano = len(numeros)

numeros.insert(0, tamano)
numeros.pop(tamano)

print(f"Lista de numeros actualizada {numeros}")