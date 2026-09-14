estudiantes_presentes = ["Ana", "Carlos", "Elena", "Lucas", "María", "Mateo", "Sofía", "Tomás"]

print(f"Lista de estudiantes presentes: {estudiantes_presentes}")

print("1. Agregar nuevo estudiante")
print("2. Eliminar a un estudiante")
eleccion = input("Elija una opcion: ")

while eleccion != "1" and eleccion != "2":
    eleccion = input("Error. Elija una opcion valida: ")

estudiante = input("Nombre: ")

if eleccion == "1":
    estudiantes_presentes.append(estudiante)    
else:
    while not estudiante in estudiantes_presentes:
        estudiante = input("Error. Ingrese un nombre valido: ")
    estudiantes_presentes.remove(estudiante)

print(f"Lista de estudiantes actualizada: {estudiantes_presentes}")