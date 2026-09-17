puntajes = [450, 1200, 875, 990, 300, 1500, 640]

print(f"Puntaje más alto: {max(puntajes)}")
print(f"Puntaje más bajo: {min(puntajes)}")

ranking = sorted(puntajes, reverse=True)
print(f"Ranking (ordenado de mayor a menor): {ranking}")

posicion = ranking.index(990)
print(f"El puntaje 990 se encuentra en la posición {posicion} del ranking")