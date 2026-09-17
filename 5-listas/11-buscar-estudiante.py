estudiantes = ["Ana", "Carlos", "Elena", "Lucas", "María", "Mateo", "Sofía", "Tomás", "Juan", "Laura"]

nombre_buscar = input("Ingrese el nombre a buscar: ")

if nombre_buscar in estudiantes:
    posicion = estudiantes.index(nombre_buscar)
    print(f"{nombre_buscar} se encuentra en la lista en la posición {posicion}")
else:
    print(f"{nombre_buscar} no está en la lista")