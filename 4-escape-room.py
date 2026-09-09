# Variables iniciales del juego
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
cerradura_bloqueada = False

# Guarda las letras ingresadas al hackear el panel
codigo_parcial = ""

# Cuenta cuántas veces seguidas se eligió "Forzar cerradura"
cont_forzar_cerradura = 0


# Pedimos el nombre del agente.
# El while se repite mientras el nombre no contenga solamente letras.
nombre_agente = ""
while not nombre_agente.isalpha():
    nombre_agente = input("Nombre de Agente: ")


# El juego continúa mientras:
# - Tengamos energía
# - Tengamos tiempo
# - Todavía no hayamos abierto las 3 cerraduras
# - La bóveda no esté bloqueada
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not cerradura_bloqueada:

    # Mostramos el estado actual del jugador
    print("")
    print(f"Energia: {energia}")
    print(f"Tiempo: {tiempo}")

    # Mostramos las opciones disponibles
    print('''
1. Forzar cerradura
2. Hackear panel
3. Descansar''')


    # Pedimos una opción y verificamos que sea un número.
    # El while continúa hasta que el usuario ingrese solamente números.
    opcion_menu = ""
    while not opcion_menu.isdigit():
        opcion_menu = input("Eleccion: ")


    # Según la opción elegida, ejecutamos una acción diferente.
    match opcion_menu:


        # --------------------------------------------------
        # OPCIÓN 1: FORZAR CERRADURA
        # --------------------------------------------------
        case "1":

            # Costo de forzar una cerradura:
            # -20 de energía y -2 de tiempo
            energia -= 20
            tiempo -= 2

            # Aumentamos el contador porque el jugador
            # eligió nuevamente "Forzar cerradura".
            cont_forzar_cerradura += 1


            # Si es la tercera vez seguida que fuerza una cerradura,
            # se activa automáticamente la alarma.
            # La cerradura NO se abre.
            if cont_forzar_cerradura == 3:
                alarma = True


            # Si todavía no llegó a la tercera vez, comprobamos
            # si tiene poca energía.
            elif energia < 40:

                print("Tiene menos de 40 de energia, hay riesgo de activar la alarma")

                # Pedimos un número para determinar si se activa
                # la alarma.
                riesgo_de_alarma = ""

                # Repetimos mientras el dato ingresado sea un número.
                while riesgo_de_alarma.isdigit():
                    riesgo_de_alarma = input("Elija un numero del 1 al 3")

                # Si el jugador elige 3, se activa la alarma.
                if riesgo_de_alarma == "3":
                    alarma = True


            # Si no se activó la alarma, conseguimos abrir una cerradura.
            if not alarma:
                cerraduras_abiertas += 1


        # --------------------------------------------------
        # OPCIÓN 2: HACKEAR PANEL
        # --------------------------------------------------
        case "2":

            # Costo de hackear el panel:
            # -10 de energía y -3 de tiempo
            energia -= 10
            tiempo -= 3

            # El for se ejecuta 4 veces para pedir las 4 letras
            # que forman parte del código.
            for i in range(4):

                # Pedimos una letra al usuario.
                letra = input(f"Ingrese la {i+1}° letra del codigo: ")

                # Agregamos la letra ingresada al código parcial.
                codigo_parcial = codigo_parcial + letra

                # Mostramos cómo va quedando el código.
                print(f"Codigo Parcial: {codigo_parcial}")


            # Si el código tiene 8 caracteres o más,
            # conseguimos abrir una cerradura.
            if len(codigo_parcial) >= 8:
                cerraduras_abiertas += 1


        # --------------------------------------------------
        # OPCIÓN 3: DESCANSAR
        # --------------------------------------------------
        case "3":

            # Descansar recupera 15 puntos de energía.
            energia += 15

            # La energía nunca puede superar los 100 puntos.
            if energia > 100:
                energia = 100

            # Descansar consume 1 unidad de tiempo.
            tiempo -= 1


            # Si la alarma está activa, descansar tiene
            # un costo adicional de 10 puntos de energía.
            if alarma:
                energia -= 10


    # Si la alarma está activa y quedan 3 o menos unidades
    # de tiempo, la bóveda se bloquea.
    if alarma and tiempo <= 3:
        cerradura_bloqueada = True



# --------------------------------------------------
# COMPROBACIÓN DEL RESULTADO DEL JUEGO
# --------------------------------------------------

# Si conseguimos abrir las 3 cerraduras, ganamos.
if cerraduras_abiertas == 3:
    print("------------")
    print("| VICTORIA |")
    print("------------")


# Si nos quedamos sin energía o sin tiempo, perdemos.
if energia <= 0 or tiempo <= 0:
    print("-----------")
    print("| DERROTA |")
    print("-----------")


# Si la alarma provocó el bloqueo de la bóveda, perdemos.
if cerradura_bloqueada:
    print("-----------")
    print("| DERROTA |")
    print("-----------")