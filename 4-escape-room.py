energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
cerradura_bloqueada = False
codigo_parcial = ""
cont_forzar_cerradura = 0

nombre_agente = ""
while not nombre_agente.isalpha():
    nombre_agente = input("Nombre de Agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not cerradura_bloqueada:
    print("")
    print(f"Energia: {energia}")
    print(f"Tiempo: {tiempo}")
    print('''
1. Forzar cerradura
2. Hackear panel
3. Descansar''')

    opcion_menu = ""
    while not opcion_menu.isdigit():
        opcion_menu = input("Eleccion: ")

    match opcion_menu:

        case "1": # Forzar cerradura
            energia -= 20
            tiempo -= 2
            cont_forzar_cerradura += 1
            
            if cont_forzar_cerradura == 3:
                alarma = True

            elif energia < 40:
                print ("Tiene menos de 40 de energia, hay riesgo de activar la alarma")
                riesgo_de_alarma = ""
                while not riesgo_de_alarma.isdigit():
                    riesgo_de_alarma = input("Elija un numero del 1 al 3")
                if riesgo_de_alarma == "3":
                    alarma = True

            if not alarma:
                cerraduras_abiertas += 1

        case "2": # Hacker panel
            energia -= 10
            tiempo -= 3
            for i in range(4):
                letra = input(f"Ingrese la {i+1}° letra del codigo: ")
                codigo_parcial = codigo_parcial + letra
                print(f"Codigo Parcial: {codigo_parcial}")

            if len(codigo_parcial) >= 8:
                cerraduras_abiertas += 1
            cont_forzar_cerradura = 0

        case "3": #Descansar
            energia += 15

            if energia > 100:
                energia = 100
            tiempo -= 1

            if alarma:
                energia -= 10
            cont_forzar_cerradura = 0

    if alarma and tiempo <= 3:
        cerradura_bloqueada = True



if cerraduras_abiertas == 3:
    print("------------")
    print("| VICTORIA |")
    print("------------")

if energia <= 0 or tiempo <= 0:
    print("-----------")
    print("| DERROTA |")
    print("-----------")

if cerradura_bloqueada:
    print("-----------")
    print("| DERROTA |")
    print("-----------")