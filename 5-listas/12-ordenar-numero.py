numeros = list()

for i in range(8):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

print(f"Lista original: {numeros}")

ordenada_ascendente = sorted(numeros)
print(f"Lista ordenada de menor a mayor: {ordenada_ascendente}")

ordenada_descendente = sorted(numeros, reverse=True)
print(f"Lista ordenada de mayor a menor: {ordenada_descendente}")