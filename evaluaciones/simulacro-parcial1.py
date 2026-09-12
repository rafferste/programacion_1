especialidades = list()
cupos = list()
eleccion_menu = ""
cantidad_especialidades = ""

while eleccion_menu != "8":
    eleccion_menu = ""
    print("""
-------------------------MENU--------------------------
1. Ingresar lista de especialidades
2. Ingresar lista de cupos disponibles por especialidad
3. Mostrar agenda
4. Consultar cupos de una especialidad
5. Listar especialidades sin cupo
6. Agregar especialidad
7. Actualizar cupos (reservar / cancelar)
8. Salir
-------------------------------------------------------
""")
    eleccion_menu = ""

    while not eleccion_menu.isdigit() or int(eleccion_menu) > 8 or int(eleccion_menu) < 1:
        eleccion_menu = input("Elija una opcion: ")

        while especialidades == [] and eleccion_menu != "1":
            print("Error: Aun no ha cargado las especialidades (opicon 1 del menu)")
            eleccion_menu = input("Elija una opcion: ")

        while not especialidades == [] and cupos == [] and eleccion_menu != "2":
            print("Error: Aun no ha cargado los cupos (opicon 2 del menu)")
            eleccion_menu = input("Elija una opcion: ")

        
    match eleccion_menu:

        #---Ingresar lista de especialidades---
        case "1":
            cantidad_especialidades = input("Cuantas especialidades desae ingresar?: ")
            while not cantidad_especialidades.isdigit() or int(cantidad_especialidades) < 1: 
                cantidad_especialidades = input("Error. Ingrese una cantidad valida: ")
            cantidad_especialidades = int(cantidad_especialidades)

            for i in range(cantidad_especialidades):
                especialidad = input(f"Especialidad {i+1}: ")
                while not especialidad.isalpha() or (especialidad in especialidades):
                    if especialidad in especialidades:
                        print("Esa especialidad ya se encuentra cargada")
                    especialidad = input("Error. Ingrese un nombre valido: ")

                especialidades.append(especialidad)
            print(f"Lista de especialidades: {especialidades}")



        #---Ingresar lista de cupos disponibles---
        case "2":
            print("Ingrese la cantidad de cupos que tiene cada especialidad:")

            for i in range(cantidad_especialidades):
                especialidad_cupos = ""

                while not especialidad_cupos.isdigit():
                    especialidad_cupos = input(f"{especialidades[i]}: ")

                cupos.append(int(especialidad_cupos))

            print(f"Lista de cupos: {cupos}")



        #---Mostrar agenda---
        case "3":
            for i in range(cantidad_especialidades):
                print(f"Especialidad: {especialidades[i]} | Cupos: {cupos[i]}")



        #---Consultar cupos de una especialidad---
        case "4":
            consulta = input("Que especialidad desea consultar?: ")
            while not consulta in especialidades:
                print("Error: Esa especialidad no se encuentra cargada")
                consulta = input("Ingrese otra: ")

            indice = especialidades.index(consulta)
            print(f"Especialidad: {especialidades[indice]} | Cupos: {cupos[indice]}")



        #---Listar especialidades sin cupos---
        case "5":
            print(f"Especialidades sin cupos: ")
            for i in range(cantidad_especialidades):
                if cupos[i] == 0:
                    print(especialidades[i])



        #---Agregar especialidad---
        case "6":
            especialidad = input("Nombre de la especialidad: ")
            while not especialidad.isalpha() or (especialidad in especialidades):
                especialidad = input("Error. Ingrese un nombre valido: ")

            especialidad_cupos = input("Cupos disponibles: ")
            while not especialidad_cupos.isdigit:
                especialidad_cupos = input("Error. Ingrese una cantidad valida: ")

            especialidades.append(especialidad)
            cupos.append(especialidad_cupos)
            cantidad_especialidades += 1



        #---Actualizar cupos (reservar / cancelar)---   
        case "7":
            consulta = input("De que especialidad es el turno?: ")
            while not consulta in especialidades:
                print("Error: Esa especialidad no se encuentra cargada")
                consulta = input("Ingrese otra: ")
            
            indice = especialidades.index(consulta)
            print("1. Reservar un turno")
            print("2. Cancerlar un turno")

            accion = ""
            while not accion.isdigit() and accion != "1" and accion != "2":
                accion = input("Elija una opcion: ")

            if accion == "1":
                cupos[indice] = cupos[indice] - 1
            else:
                cupos[indice] = cupos[indice] + 1
