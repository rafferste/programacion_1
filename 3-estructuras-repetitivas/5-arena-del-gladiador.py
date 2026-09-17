nombre = ""
while not nombre.isalpha():
    nombre = input("Nombre del Gladiador: ")
    if not nombre.isalpha():
        print("Error: Solo se permiten letras.")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
dano_pesado = 15
dano_enemigo = 12
juego_activo = True

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print('''Elige acción:
1. Ataque Pesado
2. Ráfaga Veloz
3. Curar''')

    opcion = ""
    while opcion != "1" and opcion != "2" and opcion != "3":
        opcion = input("Opción: ")
        if not opcion.isdigit() or (opcion != "1" and opcion != "2" and opcion != "3"):
            print("Error: Ingrese un número válido.")

    match opcion:
        case "1":
            if vida_enemigo < 20:
                dano_final = float(dano_pesado * 1.5)
            else:
                dano_final = dano_pesado

            vida_enemigo -= dano_final
            print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")

        case "2":
            print(">> ¡Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        case "3":
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("¡Te has curado 30 puntos de vida!")
            else:
                print("¡No quedan pociones!")

    if vida_enemigo > 0:
        vida_jugador -= dano_enemigo
        print(f"¡El enemigo te atacó por {dano_enemigo} puntos de daño!")

if vida_jugador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")