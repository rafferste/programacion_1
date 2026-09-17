operador = ""
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

opcion_menu = ""

while not operador.isalpha():
    operador = input("Nombre del operador: ")

while opcion_menu != "5":
    print('''
--- MENÚ DE TURNOS ---
1. Reservar turno
2. Cancelar turno
3. Ver agenda del día
4. Ver resumen general
5. Cerrar sistema''')

    opcion_menu = input("Elija una opción: ")

    match opcion_menu:
        case "1":
            dia = ""
            while dia != "1" and dia != "2":
                dia = input("Elegir día (1=Lunes, 2=Martes): ")

            paciente = ""
            while not paciente.isalpha():
                paciente = input("Nombre del paciente: ")

            if dia == "1":
                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                    print("Error: El paciente ya tiene un turno reservado este día.")
                elif lunes1 == "":
                    lunes1 = paciente
                    print("Turno reservado con éxito en Lunes (Turno 1).")
                elif lunes2 == "":
                    lunes2 = paciente
                    print("Turno reservado con éxito en Lunes (Turno 2).")
                elif lunes3 == "":
                    lunes3 = paciente
                    print("Turno reservado con éxito en Lunes (Turno 3).")
                elif lunes4 == "":
                    lunes4 = paciente
                    print("Turno reservado con éxito en Lunes (Turno 4).")
                else:
                    print("No hay cupos disponibles para el día Lunes.")

            elif dia == "2":
                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print("Error: El paciente ya tiene un turno reservado este día.")
                elif martes1 == "":
                    martes1 = paciente
                    print("Turno reservado con éxito en Martes (Turno 1).")
                elif martes2 == "":
                    martes2 = paciente
                    print("Turno reservado con éxito en Martes (Turno 2).")
                elif martes3 == "":
                    martes3 = paciente
                    print("Turno reservado con éxito en Martes (Turno 3).")
                else:
                    print("No hay cupos disponibles para el día Martes.")

        case "2":
            dia = ""
            while dia != "1" and dia != "2":
                dia = input("Elegir día (1=Lunes, 2=Martes): ")

            paciente = ""
            while not paciente.isalpha():
                paciente = input("Nombre del paciente a cancelar: ")

            if dia == "1":
                if lunes1 == paciente:
                    lunes1 = ""
                    print("Turno cancelado exitosamente.")
                elif lunes2 == paciente:
                    lunes2 = ""
                    print("Turno cancelado exitosamente.")
                elif lunes3 == paciente:
                    lunes3 = ""
                    print("Turno cancelado exitosamente.")
                elif lunes4 == paciente:
                    lunes4 = ""
                    print("Turno cancelado exitosamente.")
                else:
                    print("Paciente no encontrado en el día Lunes.")

            elif dia == "2":
                if martes1 == paciente:
                    martes1 = ""
                    print("Turno cancelado exitosamente.")
                elif martes2 == paciente:
                    martes2 = ""
                    print("Turno cancelado exitosamente.")
                elif martes3 == paciente:
                    martes3 = ""
                    print("Turno cancelado exitosamente.")
                else:
                    print("Paciente no encontrado en el día Martes.")

        case "3":
            dia = ""
            while dia != "1" and dia != "2":
                dia = input("Elegir día a consultar (1=Lunes, 2=Martes): ")

            if dia == "1":
                print("\n--- AGENDA LUNES ---")
                print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
                print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
                print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
                print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
            elif dia == "2":
                print("\n--- AGENDA MARTES ---")
                print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
                print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
                print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

        case "4":
            ocupados_lunes = 0
            if lunes1 != "":
                ocupados_lunes += 1
            if lunes2 != "":
                ocupados_lunes += 1
            if lunes3 != "":
                ocupados_lunes += 1
            if lunes4 != "":
                ocupados_lunes += 1

            ocupados_martes = 0
            if martes1 != "":
                ocupados_martes += 1
            if martes2 != "":
                ocupados_martes += 1
            if martes3 != "":
                ocupados_martes += 1

            disponibles_lunes = 4 - ocupados_lunes
            disponibles_martes = 3 - ocupados_martes

            print("\n--- RESUMEN GENERAL ---")
            print(f"Lunes  -> Turnos Ocupados: {ocupados_lunes} | Disponibles: {disponibles_lunes}")
            print(f"Martes -> Turnos Ocupados: {ocupados_martes} | Disponibles: {disponibles_martes}")

            if ocupados_lunes > ocupados_martes:
                print("Día con más turnos ocupados: Lunes")
            elif ocupados_martes > ocupados_lunes:
                print("Día con más turnos ocupados: Martes")
            else:
                print("Día con más turnos ocupados: Empate")

        case "5":
            pass

        case _:
            print("Error: Ingrese un número válido")