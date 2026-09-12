nombre_gladiador:str = ""
vida_gladiador:int = 100
vida_enemigo:int = 100
pociones_vida:int = 0
daño_ataque_pesado:int = 15
daño_enemigo:int = 12
turno_gladiador:bool = True

nombre_gladiador = input("Nombre del Gladiador: ")
while not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras")
    nombre_gladiador = input("Nombre del Gladiador: ")

while vida_gladiador > 0 and vida_enemigo > 0:
    #------------------------#
    #Turno Jugador
    #------------------------#
    print(f"Vida del Gladiador: {vida_gladiador}")
    print(f"Vida del Enemigo: {vida_enemigo}")
    print(f"Pociones restantes: {pociones_vida}")
    print("""
1. Ataque Pesado
2. Rafaga Veloz
3. Curar""")