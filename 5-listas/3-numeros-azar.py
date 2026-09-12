import random
lista_pares = list()
lista_impares = list()

# Generar 5 números aleatorios entre 1 y 100
lista_aleatoria = [random.randint(1, 100) for _ in range(15)]
print(lista_aleatoria)

for numero in lista_aleatoria:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f"Lista de pares tiene: {len(lista_pares)} numeros")
print(f"Lista de impares tiene: {len(lista_impares)} numeros")